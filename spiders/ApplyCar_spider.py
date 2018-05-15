#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy
import re

from tutorial.items import ApplyCarItem
'''
杭州小汽车摇号数据
'''
class ApplyCarSpider(scrapy.Spider):

    name = "apply"
    allowed_domains = ["apply.hzcb.gov.cn"]
    start_urls = []
    first_url = ''

    def __init__(self):
        for issueNumber in range(201405,201805):
            last = str(issueNumber)[-2:]
            if int(last)<13 and int(last)>0:
                self.start_urls.append(str(issueNumber))

    def start_requests(self):
        for issueNumber in self.start_urls:
            yield scrapy.Request('http://apply.hzcb.gov.cn/apply/app/status/norm/person?issueNumber='+issueNumber)

    def parse(self, response):
        list = response.xpath('//tr[@class="content_data" or @class="content_data1"]')
        month = response.xpath('//option[@selected="selected"]/text()').extract_first()
        for data in list:
            item = ApplyCarItem()
            ll = data.xpath('td/text()').extract()
            item['month'] = month
            item['no'] = ll[0]
            item['name'] = ll[1]
            yield item
            pass
        pattern = re.compile(r'(?<=\(\')\d+(?=\')')
        m = pattern.findall(response.body_as_unicode())
        print('**************',m,response.url)
        pageSize = int(m[1])
        pageNow  = int(m[2])
        if pageNow == 1:
            self.first_url = response.url
        while pageNow < pageSize:
            pageNow += 1
            url = self.first_url+'&pageNo='+str(pageNow)
            yield  scrapy.Request(url,self.parse)
            pass
