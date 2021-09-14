#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import scrapy
from  practicalone.items import PracticaloneItem

class SolutionSpider(scrapy.Spider):
    name = "Solution"
    #allowed_domains[]
    start_urls = [
        
           "http://books.toscrape.com/catalogue/the-grand-design_405/index.html",
           "http://books.toscrape.com/catalogue/the-origin-of-species_499/index.html",
           "http://books.toscrape.com/catalogue/under-the-tuscan-sun_504/index.html",
           "http://books.toscrape.com/catalogue/a-year-in-provence-provence-1_421/index.html",
        
        ]
    
    
    def parse(self, response):
        item = PracticaloneItem()
        
        item['category'] = response.xpath("//ul[@class='breadcrumb']/li[3]/a/text()").get()
        
        item['price'] = response.xpath("//p[@class='price_color']/text()").get()
        
        item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        
        item['in_stock'] = response.xpath("normalize-space(//p[@class='instock availability']/i/following::node()[1])").get()
      
        
        return item
    