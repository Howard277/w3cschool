# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from w3cschool.spiders.W3CSchoolSpider import W3CSchoolSpider
import scrapy


class W3CschoolPipeline(object):
    def process_item(self, item, spider):
        print('item内容：', item)
        return item


class W3CschoolSubPipeline(object):
    def process_item(self, item, spider):
        scrapy.Request(item['url'], callback=W3CSchoolSpider.parse_sub)
        pass
