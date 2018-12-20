from w3cschool.items import W3CschoolItem
import pickle
from scrapy import Spider, log


class W3CSchoolSpider(Spider):
    # log.start(logfile='/Users/wuketao/Downloads/w3cschool.log')
    name = 'w3cschool'
    allowed_domains = ["www.w3cschool.cn"]
    start_urls = ['http://fazhi.cpd.com.cn/']

    def parse(self, response):
        for item in response.xpath('//div[@class=news]/ul/li/a/text()').extract():
            w3citem = W3CschoolItem()
            w3citem['title1'] = item
            yield w3citem
