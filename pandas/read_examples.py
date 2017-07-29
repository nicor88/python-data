import pandas as pd
import json

df_csv = pd.read_csv('data/FL_insurance_sample.csv')

# get a dataset from here http://jsonstudio.com/resources/
df_json = pd.read_json('data/world_bank.json', lines=True)
