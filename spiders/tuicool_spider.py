#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy
import random
from scrapy.conf import settings
from tutorial.items import TuiCoolItem

class TuicoolSpider(scrapy.Spider):
    name = "tuicool"
    allowed_domains = ["tuicool.com"]
    start_urls = ['https://www.tuicool.com/a/']

    cookie = settings['COOKIE']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,cookies=self.cookie) # 通过meta参数添加代理


    def parse(self, response):
        currentpage_movie_items = response.xpath('//div[@class="list_article_item"]')
        for movie_item in currentpage_movie_items:
            movie = TuiCoolItem()

            movie['href'] = movie_item.xpath('div[@class="aricle_item_info"]/div[@class="title"]/a/@href').extract_first()
            movie['title'] = movie_item.xpath('div[@class="aricle_item_info"]/div[@class="title"]/a/@title').extract_first()
            movie['img'] = movie_item.xpath('div[@class="article_thumb_image"]/img/@src').extract_first()
            movie['tip'] = movie_item.xpath('normalize-space(div[@class="aricle_item_info"]//div[@class="tip"]/span/text())').extract()
            yield movie
            pass
        ##下面的代码应该是个分页的，但是目标网页没有分页的需要！！！！！
        nextPage=response.xpath('//li[@class="next"]/a/@href').extract_first()
        if nextPage:
            url = response.urljoin(nextPage)
            yield  scrapy.Request(url,self.parse)
        pass
