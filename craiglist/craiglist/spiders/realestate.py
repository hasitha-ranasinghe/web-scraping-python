# -*- coding: utf-8 -*-
import scrapy


class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['https://newyork.craigslist.org/d/real-estate/search/rea']
    start_urls = ['http://https://newyork.craigslist.org/d/real-estate/search/rea/']

    def parse(self, response):
        print("\n")
        print("HTTP STATUS: "+str(response.status))
        print(response.css("title::text").get())
        print("\n")
