#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy

from tutorial.items import PaynewsItem
'''
中国支付网信息
'''
class PaynewsSpider(scrapy.Spider):
    name = "paynews"
    allowed_domains = ["paynews.net"]
    start_urls = [
    'http://paynews.net/portal.php?mod=list&catid=96',
    'http://paynews.net/news/zhifu/',
    'http://paynews.net/news/qiye/',
    'http://paynews.net/news/pinglun/'
    ]

    def parse(self, response):
        currentpage_movie_items = response.xpath('//dl[@class="bbda cl"]')
        for movie_item in currentpage_movie_items:
            movie = PaynewsItem()
            # link title outline time pic_url
            movie['link'] = movie_item.xpath('dt/a/@href').extract_first()
            movie['time'] = movie_item.xpath('dd/span/text()').extract_first()
            movie['title'] = movie_item.xpath('dt/a/text()').extract_first()
            # movie['outline'] = movie_item.xpath('dd[@class="xs2 cl"]/text()').extract_first()
            movie['pic_url'] = movie_item.xpath('dd/div/a/img/@src').extract_first()
            yield movie
            pass

        nextPage=response.xpath('//a[@class="nxt"]/@href').extract_first()
        if nextPage:
            yield  scrapy.Request(nextPage,self.parse)
        pass
