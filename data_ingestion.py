import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://python_user:python_user@localhost:5432/energy')

df = pd.read_csv('energy_dataset.csv')
df.to_sql('t_energy_data', engine, schema='raw')

df = pd.read_csv('weather_features.csv')
df.to_sql('t_weather_data', engine, schema='raw')
