# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:29:24 2020

@author: tngo0508
"""

import scrapy
from practicalone.items import PracticaloneItem

class SecondSpider(scrapy.Spider):
    name = "Books2"
    start_urls = [
        "https://books.toscrape.com/",
        "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
    ]

    def parse(self, response):
        item = PracticaloneItem()
        #item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract() 
        #item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        
        return item