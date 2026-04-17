from sqlalchemy import create_engine, text 
from urllib.parse import quote_plus
import pandas as pd
import os
from dotenv import load_dotenv
import logging 
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent / 'config' / '.env'
load_dotenv(env_path)

def get_engine():
    user = os.getenv('user')
    password = os.getenv('password')
    database = os.getenv('database')
    host = os.getenv('host')

    logging.info(f"→ Conectando em {host}:5432/{database}")
    return create_engine(f"postgresql+psycopg2://{user}:{quote_plus(password)}@{host}:5432/{database}")

def load_weather_data(table_name:str, df):
    engine = get_engine()
    df.to_sql(
        name=table_name, 
        con=engine, 
        if_exists='append', 
        index=False
    )
    
    logging.info(f"✓ Dados carregados com sucesso na tabela {table_name}.\n")

    df_check = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    logging.info(f"Total de registros: {len(df_check)}\n")
    