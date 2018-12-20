# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class W3CschoolItem(scrapy.Item):
    title1 = scrapy.Field()
    title2 = scrapy.Field()
    description = scrapy.Field()
    pass


class CainiaoItem(scrapy.Item):
    content = scrapy.Field()
    pass
