from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd

option = webdriver.ChromeOptions()

# Run the argument with incognito
option.add_argument(' — incognito')
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=option)

driver.get('https://www.lazada.sg/#')

# Wait 30 seconds for page to load and extract the element after it loads
timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "Level_1_Category_No1")))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()


# find_elements_by_xpath returns an array of selenium objects.
category_element = driver.find_element(By.ID,'Level_1_Category_No1').text;
print("category element ",category_element)

# Take the list of li in the ul
# list_category_elements = driver.find_element(By.XPATH,'//*[@id="J_icms-5000498-1511516689962"]/div/ul')
# links = list_category_elements.find_elements(By.CLASS_NAME,"lzd-site-menu-root-item")
# print('length of links are: ', len(links))
# for i in range(len(links)):
#     print("element in list ",links[i].text)

# Clicking toys menu to find the right one
# You might receive error if you just perform element.click(). This is due to the element might not actionable according to DOM
# element = driver.find_elements_by_class_name('J_ChannelsLink')[1]
# webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

# try:
#     WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "title_wrapper")))
# except TimeoutException:
#     print('Timed out waiting for page to load')
#     driver.quit()

# Once we are in, let us extract all of the product elements then names
# product_titles = driver.find_elements_by_class_name('title')
# for title in product_titles:
#     print(title.text)

# Let us make a panda dataframe of title, price
# product_containers = driver.find_elements_by_class_name('product_container')
#
# product_titles = list()
# pack_sizes = list()
# product_prices = list()
# rating_counts = list()
#
# for container in product_containers:
#     product_titles.append(container.find_element_by_class_name('title').text)
#     pack_sizes.append(container.find_element_by_class_name('pack_size').text)
#     product_prices.append(container.find_element_by_class_name('product_price').text)
#     rating_counts.append(container.find_element_by_class_name('ratings_count').text)
#
# data = {'product_title': product_titles, 'pack_size': pack_sizes,'product_price': product_prices, 'rating_count': rating_counts}
# df_product = pd.DataFrame.from_dict(data)
#
# print(df_product.head())


# Exporting the data into csv
# df_product.to_csv('product_info.csv')
