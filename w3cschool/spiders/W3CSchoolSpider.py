from w3cschool.items import W3CschoolItem
import scrapy


class W3CSchoolSpider(scrapy.Spider):
    name = 'w3cschool'  # 设置spider的name
    allowed_domains = ["fazhi.cpd.com.cn"]  # 设置运行爬取的域名集合
    start_urls = ['http://fazhi.cpd.com.cn/']  # 设置爬取的其实位置

    # 初始爬取处理函数
    def parse(self, response):
        for item in response.xpath("//div[@class='news']/ul/li/a"):
            href = item.xpath('@href').extract()[0]  # 获取href属性
            text = item.xpath('text()').extract()[0]  # 获取a标签中的文本
            w3citem = W3CschoolItem()
            url = self.start_urls[0] + href
            w3citem['data'] = text
            w3citem['url'] = url
            yield w3citem

    # 子爬取处理函数
    def parse_sub(self, response):
        title = response.xpath("//h1[@class='hetitle_01']/gettitle/text()").extract()[0]
        body = response.xpath("//div[@id='fz_test']/div/table/tr/td/text()").extract()
        entity = {'title': title, 'body': body}
        print('entity内容：', entity)
