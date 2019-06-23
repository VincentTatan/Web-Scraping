import pandas as pd
import sqlite3
from sqlalchemy import create_engine

conn = sqlite3.connect("amazon.db")
disk_engine = create_engine('sqlite:///amazon_alchemy.db')
c = conn.cursor()

def read():
    df = pd.read_sql_query("select * from amazon_product;", conn)
    print(df)
    return df

def write_values(id,link,product_title,product_price,category):
    c.execute("INSERT INTO amazon_product VALUES "
              "(CURRENT_TIMESTAMP,id, link,product_title,product_price,category)")

def write_from_df_with_sqlite3(df):
    for index, row in df.iterrows():
        c.execute(
        '''
            INSERT INTO amazon_product VALUES 
              (CURRENT_TIMESTAMP,?,?,?,?,?)
        ''',
            (row['id'], row['link'],row['product_title'],row['product_price'],
            row['category'])
        )

def write_from_df_with_alchemy(df):
    df.to_sql('amazon_product', disk_engine, if_exists='append')



