import pandas as pd
from pkg_resources import resource_string
import ruamel_yaml as yaml

from sqlalchemy import create_engine

postgres_cfg = yaml.load(resource_string('config', 'settings.yml'))['postgres']

postgres_engine = create_engine('postgresql://{user}:{password}@{hostname}:5432/{db}'
                                .format(user=postgres_cfg['user'],
                                        password=postgres_cfg['password'],
                                        hostname=postgres_cfg['hostname'],
                                        db=postgres_cfg['db']))

# tables = pd.read_sql('SELECT * FROM pg_catalog.pg_tables;', con=postgres_engine)

film_df = pd.read_sql('SELECT * FROM film;', con=postgres_engine)
film_category_df = pd.read_sql('SELECT * FROM film_category;', con=postgres_engine)
category_df = pd.read_sql('SELECT * FROM category;', con=postgres_engine)
film_with_category = pd.merge(pd.merge(film_df, film_category_df, on=['film_id'], how='inner'), category_df, on=['category_id'], how='inner')
film_with_category = film_with_category.rename(columns={'name': 'category'})
# film_with_category = film_with_category.rename(columns={'name': 'category'})

film_by_category_qry = """select category.name as category_name,
count(distinct film.title) as total_film,
string_agg(film.title,',')
from    film
join    film_category using(film_id)
join    category using(category_id)
group by category.name
order by category_name;
"""
df = pd.read_sql(film_by_category_qry, con=postgres_engine)

film_by_category_qry_with_filter = """select category.name as category_name,
count(distinct film.title) as total_film,
string_agg(film.title,',')
from    film
join    film_category using(film_id)
join    category using(category_id)
where film.title = '{title}'
group by category.name
order by category_name;
"""

df_filtered = pd.read_sql(film_by_category_qry_with_filter.format(title='Zorro Ark'), con=postgres_engine)
