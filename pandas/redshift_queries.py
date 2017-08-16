import pandas as pd
from pkg_resources import resource_string
import ruamel_yaml as yaml

from sqlalchemy import create_engine

cfg = yaml.load(resource_string('config', 'settings.yml'))['redshift']
engine = create_engine(f'postgresql://{cfg["user"]}:{cfg["password"]}@{cfg["hostname"]}:{cfg["port"]}/{cfg["db"]}')

tables = pd.read_sql('SELECT * FROM pg_catalog.pg_tables;', con=engine)

