from pkg_resources import resource_string
import ruamel_yaml as yaml
import logging

import pandas as pd
from sqlalchemy import create_engine
from tweepy import OAuthHandler
from tweepy import API

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

twitter_cfg = yaml.load(resource_string('config', 'twitter.yml'))
postgres_cfg = yaml.load(resource_string('config', 'settings.yml'))['postgres']

postgres_engine = create_engine('postgresql://{user}:{password}@{hostname}:5432/{db}'
                                .format(user=postgres_cfg['user'],
                                        password=postgres_cfg['password'],
                                        hostname=postgres_cfg['hostname'],
                                        db=postgres_cfg['db']))

auth = OAuthHandler(twitter_cfg['consumer_key'], twitter_cfg['consumer_secret'])
auth.set_access_token(twitter_cfg['access_token'], twitter_cfg['access_secret'])
twitter_api = API(auth)


def get_tweets_for_user(*, user_name, tweets_count=10):
    tweets = twitter_api.user_timeline(count=tweets_count, screen_name=user_name)
    for status in tweets:
        log.debug(status._json)
        filtered_status = {s: status._json[s] for s in ['created_at', 'text', 'user', 'id']}
        filtered_status['user_screen_name'] = filtered_status['user']['screen_name']
        filtered_status['user_id'] = filtered_status['user']['id']
        filtered_status['tweet_id'] = filtered_status.pop('id')
        filtered_status.pop('user', None)
        log.debug(filtered_status)
        yield filtered_status


def save_tweets_to_db(*, db_engine, tweets, tweets_table='tweets'):
    tweets_df = pd.DataFrame.from_dict(tweets)
    try:
        tweets_df.to_sql(con=db_engine, name=tweets_table, if_exists='append', index=False)
    except Exception as e:
        print(e)

user_tweets = get_tweets_for_user(user_name='nicorc88', tweets_count=12)
# save_tweets_to_db(db_engine=postgres_engine, tweets=user_tweets)
