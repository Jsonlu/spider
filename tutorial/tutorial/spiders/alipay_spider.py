#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy
import random
import re
from w3lib.html import remove_tags
from tutorial.items import AliPayItem

def go_remove_tag(value):
    if value:
        content = remove_tags(value)
        return re.sub(r'[\t\r\n\s]', '', content)
    else:
        return None

'''
需要支付宝登录后的cookie
'''
class AlipaySpider(scrapy.Spider):
    name = "alipay"
    allowed_domains = ["lab.alipay.com"]
    start_urls = ['https://lab.alipay.com/consume/record/items.htm']

    #登录后的cookie
    cookie = {'ALIPAYJSESSIONID':'RZ25aLlLAqaY0uFXRBpFpFkaAe6RwEauthRZ25GZ00'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,cookies=self.cookie) # 通过meta参数添加代理

    def parse(self, response):
        list = response.xpath('//tr[@class="record-list"]')
        for i in list:
            item = AliPayItem()
            item['number'] = go_remove_tag(i.xpath('td[@class="number"]/div/text()').extract_first())
            item['time'] = go_remove_tag(i.xpath('td[@class="time"]/text()').extract_first())
            item['info'] = go_remove_tag(i.xpath('td[@class="info"]/ul/li/text()').extract_first())
            item['amountIncome'] = i.xpath('td[@class="amount income"]/text()').extract_first()
            item['amountOutlay'] = i.xpath('td[@class="amount outlay"]/text()').extract_first()
            item['balance'] = i.xpath('td[@class="balance"]/text()').extract_first()
            item['fromAddr'] = i.xpath('td[@class="from"]/ul/li/text()').extract_first()
            item['detail'] = go_remove_tag(i.xpath('td[@class="detail"]/a/@href').extract_first())
            yield item
            pass

        # nextPage=response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if nextPage:
        #     url = response.urljoin(nextPage)
        #     yield  scrapy.Request(url,self.parse)
        # pass
