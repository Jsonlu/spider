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
    start_urls = ['http://apply.gzjt.gov.cn/apply/norm/personQuery.html']

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

        # 此处配置爬取所有还是指定
        # allMonth = response.xpath('//option/text()').extract()
        allMonth = ['201804','201803']
        del allMonth[0]
        for m in allMonth:
            body = {'issueNumber':str(m),'pageNo':'2'}
            print('*****************',body)
            yield  scrapy.FormRequest(url=response.url,method="POST",formdata=body,callback=self.post)
        pass

    def post(self,response):
        list = response.xpath('//tr[@style="color:red;font-size: 16px;font-weight: bolder;"]')
        month = response.xpath('//option[@selected="selected"]/text()').extract_first()
        for data in list:
            item = ApplyCarItem()
            ll = data.xpath('td/text()').extract()
            item['month'] = month
            item['no'] = ll[0]
            item['name'] = ll[1]
            yield item

        pageSize = response.xpath('//span[@class="f_orange"]/text()').extract_first()
        pageSize = int(pageSize)
        pageNow  = response.xpath('//input[@id="num"]/@value').extract_first()
        pageNow  = int(pageNow)

        while pageNow < pageSize:
            pageNow += 1
            body = {'issueNumber':month,'pageNo':str(pageNow)}
            print('*****************',body)
            yield  scrapy.FormRequest(url=response.url,method="POST",formdata=body,callback=self.post)
        pass
