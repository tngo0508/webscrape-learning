# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:19:18 2020

@author: tngo0508
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://sdsclub.com/')
time.sleep(5)


driver.find_element_by_xpath('/html/body/header/div/div/div[2]/a').click()
time.sleep(5)

driver.find_element_by_id('username')
dirver.find_element_by_id('password')

username.send_keys('username')
username.send_keys('password')

driver.quit()