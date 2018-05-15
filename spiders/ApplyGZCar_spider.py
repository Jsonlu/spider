#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy
import re

from tutorial.items import ApplyCarItem
'''
广州小汽车摇号数据
'''
class ApplyCarSpider(scrapy.Spider):

    name = "applyGZ"
    allowed_domains = ["gov.cn"]
    start_urls = []
    first_url = None

    def __init__(self):
        for issueNumber in range(201804,201805):
            last = str(issueNumber)[-2:]
            if int(last)<13 and int(last)>0:
                self.start_urls.append(str(issueNumber))

    def start_requests(self):
        for issueNumber in self.start_urls:
            yield scrapy.Request('http://apply.gzjt.gov.cn/apply/norm/personQuery.html?issueNumber='+issueNumber)

    def parse(self, response):
        list = response.xpath('//tr[@style="color:red;font-size: 16px;font-weight: bolder;"]')
        month = response.xpath('//option[@selected="selected"]/text()').extract_first()
        for data in list:
            item = ApplyCarItem()
            ll = data.xpath('td/text()').extract()
            item['month'] = month
            item['no'] = ll[0]
            item['name'] = ll[1]
            yield item
            pass
        print('**************',response.url)
        pageSize = response.xpath('//span[@class="f_orange"]/text()').extract_first()
        pageSize = int(pageSize)
        pageNow  = response.xpath('//input[@id="num"]/@value').extract_first()
        pageNow  = int(pageNow)

        if pageNow == 1:
            self.first_url = response.url
        while pageNow < pageSize:
            pageNow += 1
            url = self.first_url+'&pageNo='+str(pageNow)
            yield  scrapy.Request(url,self.parse)
            pass
