#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy
import re

from tutorial.items import ApplyCarItem
'''
杭州/天津/深圳小汽车摇号数据
天津，tjjttk
杭州，hzcb
深圳，sztb
'''
class ApplyCarSpider(scrapy.Spider):

    name = "apply"
    allowed_domains = ["gov.cn"]
    city = 'hzcb'
    start_urls = ['http://apply.'+city+'.gov.cn/apply/app/status/norm/person']


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

        # 此处配置爬取所有  还是指定月份
        allMonth = response.xpath('//option/text()').extract()
        # allMonth = ['201804','201803']
        del allMonth[0]

        for m in allMonth:
            body = {'issueNumber':str(m),'pageNo':'2'}
            print('*****************',body)
            yield  scrapy.FormRequest(url=response.url,method="POST",formdata=body,callback=self.post)
        pass


    def post(self, response):
        list = response.xpath('//tr[@class="content_data" or @class="content_data1"]')
        month = response.xpath('//option[@selected="selected"]/text()').extract_first()
        for data in list:
            item = ApplyCarItem()
            ll = data.xpath('td/text()').extract()
            item['month'] = month
            item['no'] = ll[0]
            item['name'] = ll[1]
            yield item
        pattern = re.compile(r'(?<=\(\')\d+(?=\')')
        m = pattern.findall(response.body_as_unicode())
        pageSize = int(m[1])
        pageNow  = int(m[2])
        while pageNow < pageSize:
            pageNow += 1
            body = {'issueNumber':month,'pageNo':str(pageNow)}
            print('*****************',body)
            yield  scrapy.FormRequest(url=response.url,method="POST",formdata=body,callback=self.post)
        pass
