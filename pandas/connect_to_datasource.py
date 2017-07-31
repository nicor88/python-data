import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

df = pd.read_sql('SELECT * FROM pg_catalog.pg_tables;', con=engine)
