# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:35:18 2020

@author: tngo0508
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument("--window-size=1543,852")

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://sdsclub.com/')

time.sleep(5)

button_one = driver.find_element_by_xpath('//*[@id="menu-item-456"]/a').click()
time.sleep(5)

button_two = driver.find_element_by_xpath(
    '//*[@id="category-career"]/div/div[2]/div[4]/div/figure/a/img').click()
time.sleep(15)

button_two = driver.find_element_by_class_name('close-icon').click()
time.sleep(5)

# add parser
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# add scrape info
scrape_one = [i.text for i in soup.findAll('span', {'class': 'desc'})]
scrape_two = [i.text for i in soup.findAll(
    'div', {'class': 'single-path-article-content'})]
scrape_three = [i.text for i in soup.findAll('p', {'class': 'name'})]

df = pd.DataFrame(scrape_one)
df_two = pd.DataFrame(scrape_two)
df_three = pd.DataFrame(scrape_three)


print(df, df_two, df_three)

time.sleep(10)

driver.quit()

df_scrape_one_clean = df.replace('\n', ' ',)
df_scrape_two_clean = df_two.replace('\n', ' ',)
df_scrape_three_clean = df_three.replace('\n', ' ',)
clean_stack = pd.concat([df_scrape_one_clean, df_scrape_two_clean, df_scrape_three_clean], axis=1)