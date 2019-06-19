import sqlite3

sqlite_file = 'amazon.sqlite'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

column_names=['id','link','product_title','product_price','category']

# Creating the new SQLite table with 5 column
c.execute('''
    CREATE TABLE amazon_product (
    time date_time ,
    id INTEGER ,
    link TEXT NOT NULL,
    product_title TEXT NOT NULL,
    product_price DOUBLE NOT NULL,
    category TEXT NOT NULL,
    PRIMARY KEY (time, id)
    );
    ''')

# c.execute('ALTER TABLE amazon_product ADD CONSTRAINT PK_PROD PRIMARY KEY (time, id);')

try:
    c.execute("INSERT INTO amazon_product VALUES (CURRENT_TIMESTAMP,1, 'www.test1.com','product_test_1','23.3','testing')")
    c.execute("INSERT INTO amazon_product VALUES (CURRENT_TIMESTAMP,2, 'www.test2.com','product_test_2','43.3','testing')")
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column ')


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()