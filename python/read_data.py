import pandas as pd
import psycopg2 as pg

engine = pg.connect("dbname='mydb' user='postgres' host='localhost' port='5432' password='test'")
df = pd.read_sql('select * from item', con=engine)
print(df)
