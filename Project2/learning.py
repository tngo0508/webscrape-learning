# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:24:22 2020

@author: tngo0508
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('https://quotes.toscrape.com/')
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)

soup = BeautifulSoup(r.content, 'lxml')

quotes = soup.find_all("div", class_="quote")
for x in quotes:
    print(x.find('span').text)
    
tags = soup.find_all("div", class_="tags")
for x in tags:
    print(x.text)