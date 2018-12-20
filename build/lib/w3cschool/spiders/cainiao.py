# -*- coding: utf-8 -*-
import scrapy
from w3cschool.items import CainiaoItem


class CainiaoSpider(scrapy.Spider):
    name = 'cainiao'
    allowed_domains = ['cainiao.com']
    start_urls = ['http://192.168.13.117/api/city/findAll']

    def parse(self, response):
        cainiao = CainiaoItem()
        cainiao['content'] = '测试'
        yield cainiao
