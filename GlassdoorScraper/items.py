# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassdoorscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    OverallRating = scrapy.Field()
    Worklife = scrapy.Field()
    CareerOps = scrapy.Field()
    Compensation = scrapy.Field()
    SeniorManagement = scrapy.Field()
    CultureValues = scrapy.Field()
    CEO_Opinion = scrapy.Field()
    Outlook = scrapy.Field()
    Recommendation = scrapy.Field()
    Pros = scrapy.Field()
    Cons = scrapy.Field()
    Feedback = scrapy.Field()
    Title = scrapy.Field()
    
    
