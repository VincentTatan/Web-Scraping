from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from random import  shuffle
import pandas as pd
import time

option = webdriver.ChromeOptions()

# Run the argument with incognito
option.add_argument(' — incognito')
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=option)

link_list =[
'https://www.amazon.com/Gillette-Fusion-ProShield-Refills-Razors/dp/B0168MB6SS?ref_=Oct_DLandingS_PC_7e8aa158_2&smid=ATVPDKIKX0DER&th=1',
'https://www.amazon.com/Gillette-Mach3-Razor-Blades-Refills/dp/B0039LMTBA?ref_=Oct_BSellerC_13271080011_1&pf_rd_p=c85fdb71-727d-58f5-9209-98379c35a68f&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=13271080011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=GMTB1EXXMWY98TYQ6G8H&th=1',
'https://www.amazon.com/Gillette-Mach3-Handle-Refills-Packaging/dp/B06X9V77XY?ref_=Oct_RAsinC_Ajax_13271080011_2&pf_rd_r=GMTB1EXXMWY98TYQ6G8H&pf_rd_p=c85fdb71-727d-58f5-9209-98379c35a68f&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=13271080011&pf_rd_m=ATVPDKIKX0DER',
'https://www.amazon.com/Made-Shaving-Razor-Blades-12-Count/dp/B07N7SFZ9S?ref_=Oct_TopRatedC_13271080011_0&pf_rd_p=c85fdb71-727d-58f5-9209-98379c35a68f&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=13271080011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=GMTB1EXXMWY98TYQ6G8H&th=1',
'https://www.amazon.com/Schick-Hydrate-Refill-Blades-Refills/dp/B00I1F2I3I?ref_=Oct_TopRatedC_13271080011_3&pf_rd_p=c85fdb71-727d-58f5-9209-98379c35a68f&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=13271080011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=GMTB1EXXMWY98TYQ6G8H&pf_rd_r=GMTB1EXXMWY98TYQ6G8H&pf_rd_p=c85fdb71-727d-58f5-9209-98379c35a68f'
]

# Shuffling to avoid being detected by Amazon
shuffle(link_list)

# Creating lists of features interested
product_title_list = list()
product_price_list = list()
category_list = list()

# Getting the start time to track on time required
start = time.time()

# -------------------------------Web Scraping-------------------------------
for link in link_list:
    # Open the url
    driver.get(link)

    # Wait 30 seconds for page to load and extract the element after it loads
    timeout = 30
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "productTitle")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()

    # -------------------------------Product title-------------------------------
    # find_elements_by_id returns an array of selenium objects.
    product_title = driver.find_element(By.ID,'productTitle').text;
    print("product title ",product_title)
    product_title_list.append(product_title)

    # -------------------------------Product price-------------------------------
    # This will return the product price, if product price of priceblock is not found, move on to the other element
    try:
        product_price = driver.find_element(By.XPATH,'//*[@id="priceblock_snsprice_Based"]/span').text
    except:
        product_price = driver.find_element(By.XPATH, '//*[@id="priceblock_ourprice"]').text

    print("product price ",product_price)
    product_price_list.append(product_price)

    # -------------------------------Category     -------------------------------
    # This will return the category of the product
    breadcrumb_container = driver.find_element(By.XPATH,'//*[@id="wayfinding-breadcrumbs_container"]')
    categories = list()
    categories_web_element = breadcrumb_container.find_elements(By.CLASS_NAME,'a-link-normal')
    for element in categories_web_element:
        categories.append(element.text)

    # This will join the list with ,
    category = '> '.join(categories)
    print("category ",category)
    category_list.append(category)





# Let us make a panda dataframe of title, price
data = {'link':link_list,'product_title': product_title_list,'product_price': product_price_list, 'category': category_list}
df_product = pd.DataFrame.from_dict(data)
print(df_product.head())

# Exporting the data into csv
df_product.to_csv('product_info_amazon.csv')

# Generate time tracker print
end = time.time()
print('for end-start')
print("For {} links, the time taken is {}".format(len(link_list), end-start))