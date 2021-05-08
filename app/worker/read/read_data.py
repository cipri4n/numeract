import pandas as pd
import psycopg2 as pg
import os
from dotenv import load_dotenv



def duration_item_id(item_id):
    # collecting secrets from .env file
    path = 'C:/Users/Ciprian/Desktop/test/python/db.env'
    load_dotenv(dotenv_path=path,verbose=True)
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_DB = os.environ.get("POSTGRES_DB")

    # connecting to postgres database
    engine = pg.connect(dbname=POSTGRES_DB , user=POSTGRES_USER , host='localhost', port='5432' ,password=POSTGRES_PASSWORD)
    df = pd.read_sql('select * from Item', con=engine)



    return df.loc[df['item_id'] == item_id]['duration'].iloc[0]
