# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:13:04 2020

@author: tngo0508
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()


def site_login():
    driver.get('https://www.superdatascience.com/login')
    time.sleep(5)

    driver.find_element_by_xpath('//*[@id="cookiescript_close"]').click()
    time.sleep(3)
    driver.find_element_by_name('email').send_keys('THISISMYEMAIL')
    driver.find_element_by_name('password').send_keys('THISISMYPASSWORD')
    driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div[1]/div/div/form/button').click()
    
    
site_login()
time.sleep(20)

driver.quit()