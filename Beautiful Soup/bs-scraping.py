from bs4 import BeautifulSoup
import requests
import pandas as pd

# Add header and  url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
# url = "https://en.wikipedia.org/wiki/List_of_national_capitals"
url = "https://www.amazon.com/"
r = requests.get(url)

# Initiate beautiful and list element to extract all the rows in the table
soup = BeautifulSoup(r.content, "html.parser")
table = soup.find_all('table')[1]
print("table is ", table)
rows = table.find_all('tr')
row_list = list()

# Iterate through all of the rows in table and get through each of the cell to append it into rows and row_list
for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)
    print("Row is ", row)

# Create Pandas Dataframe and print it
df_bs = pd.DataFrame(row_list,columns=['City','Country','Notes'])
df_bs.set_index('Country',inplace=True)
print(df_bs.head())

# Exporting the data into csv
df_bs.to_csv('beautifulsoup.csv')

