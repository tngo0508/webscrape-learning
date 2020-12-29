# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#section 1
import scrapy

#section 2
class FirstSpider(scrapy.Spider):
    name = "Books"
    start_urls = [
        "https://books.toscrape.com/",
        "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
    ]

    #section 3
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'books-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)