import pandas as pd
import sqlite3


conn = sqlite3.connect("amazon.db")

def read_sql():
    df = pd.read_sql_query("select * from amazon_product;", conn)
    print(df)
    return df

def write_sql(id,link,product_title,product_price,category):
    c = conn.cursor()
    c.execute("INSERT INTO amazon_product VALUES "
              "(CURRENT_TIMESTAMP,id, link,product_title,product_price,category)")



