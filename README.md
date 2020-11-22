Web scraping is a very powerful tool to learn for any data professional. With web scraping the entire internet becomes your database. In this repository how to parse a web page into a data file (csv) using a Python package called BeautifulSoup Two ways to extract data from a website:

1.Use the API of the website (Best way) The data on the websites are unstructured,

Sadly, not all websites provide an API

2.Web Scraping: Web scraping is an automated method used to extract useful information from the websites focuses on the transformation of unstructured data (HTML format) on the web into structured data.

STEPS: To extract data using web scraping with python,you need to follow these basic steps:

1.Find the URL that you want to scrape

2.Check wheather is it legal to scrap from that website Goto www.URL/robots.txt if you are using Scrapy you no need to worry because it automatically allow only Legal links. in Settings.py ROBOTSTXT_OBEY=False

3.Inspecting the Website

4.Find the data you want to extract

5.Write the code

6.Run the code and extract the data

7.Store the data in the required format

Need of Web Scraping

Price Comparison: Services such as ParseHub use web scraping to collect data from online shopping websites and use it to compare the prices of products.

Email address gathering: Many companies that use email as a medium for marketing, use web scraping to collect email ID and then send bulk emails.

travel recommendation:ow about scraping a few travel recommendation sites, pull out comments about various do to things and see which property is getting a lot of positive responses from the users! The list of use cases is endless.

Social Media Scraping: Web scraping is used to collect data from Social Media websites such as Twitter to find out what’s trending.

Research and Development: Web scraping is used to collect a large set of data (Statistics, General Information, Temperature, etc.) from websites, which are analyzed and used to carry out Surveys or for R&D.

Job listings: Details regarding job openings, interviews are collected from different websites and then listed in one place so that it is easily accessible to the user.

Is Web Scraping legal?

To know whether a website allows web scraping or not, you can look at the website’s “robots.txt” file. You can find this file by appending “/robots.txt” to the URL that you want to scrape.
