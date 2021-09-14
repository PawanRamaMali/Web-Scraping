#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:21:01 2020

@author: jordansauchuk
"""


import scrapy
from practicalone.items import PracticaloneItem

class SecondSpider(scrapy.Spider):
    name = "Books2"
    start_urls = [
        
        "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
        
    ]
    
    def parse(self, response):
        item = PracticaloneItem()
        #item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        #item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
        
        return item