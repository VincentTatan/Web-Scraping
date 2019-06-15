from bs4 import BeautifulSoup
import requests
url = "https://www.google.com"
# Add header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
r = requests.get(url, headers=headers)
print(r) # print request to see if Response 200
soup = BeautifulSoup(r.content, "html.parser")

print(soup)