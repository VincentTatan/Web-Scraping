import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn = sqlite3.connect("lazada_alchemy.db")
disk_engine = create_engine('sqlite:///lazada_alchemy.db')
c = conn.cursor()

def read():
    df = pd.read_sql_query("select * from lazada_product;", conn)
    return df

def write_values(id,link,product_title,product_price,category):
    c.execute("INSERT INTO lazada_product VALUES "
              "(CURRENT_TIMESTAMP,id, link,product_title,product_price,category)")

def write_from_df_with_sqlite3(df):
    for index, row in df.iterrows():
        c.execute(
        '''
            INSERT INTO lazada_product VALUES 
              (CURRENT_TIMESTAMP,?,?,?,?,?)
        ''',
            (row['id'], row['link'],row['product_title'],row['product_price'],
            row['category'])
        )

def write_from_df_with_alchemy(df):
    #Adding Timestamp
    df['datetime'] = pd.Timestamp("today").strftime("%m/%d/%Y")

    # Appending the results to lazada_producct
    df.to_sql('lazada_product', disk_engine, if_exists='replace')
