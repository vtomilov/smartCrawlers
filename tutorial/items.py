# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DmozItem(scrapy.Item):
    Title = scrapy.Field()
    Price = scrapy.Field()
    Image_Src = scrapy.Field()
    Description = scrapy.Field()
    SKU = scrapy.Field()
    Quantity = scrapy.Field()
    Vendor = scrapy.Field()
    Type = scrapy.Field()
