# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:52:56 2020

@author: tngo0508
"""

import scrapy
from practicalone.items import PracticaloneItem

class SolutionSpider(scrapy.Spider):
    name = "Solution"
    #allowed_domains[]
    start_urls = [
        "https://books.toscrape.com/catalogue/the-origin-of-species_499/index.html",
        "https://books.toscrape.com/catalogue/a-year-in-provence-provence-1_421/index.html",
        "https://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html",
        "https://books.toscrape.com/catalogue/the-road-to-little-dribbling-adventures-of-an-american-in-britain-notes-from-a-small-island-2_277/index.html"
    ]
    
    def parse(self, response):
        item = PracticaloneItem()
        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        item['in_stock'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
        
        return item