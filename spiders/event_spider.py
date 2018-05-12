#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy

from tutorial.items import EventItem

class EventSpider(scrapy.Spider):
    name = "event"
    allowed_domains = ["douban.com"]
    start_urls = ['https://www.douban.com/location/hangzhou/events/future-all']

    def parse(self, response):
        currentpage_movie_items = response.xpath('//li[@class="list-entry" and @itemscope]')
        for movie_item in currentpage_movie_items:
            movie = EventItem()
            movie['img'] = movie_item.xpath('div[@class="pic"]/a/@href').extract_first()
            movie['title'] = movie_item.xpath('div[@class="info"]/div[@class="title"]/a/@title').extract_first()
            movie['href'] = movie_item.xpath('div[@class="info"]/div[@class="title"]/a/@href').extract_first()
            movie['startDate'] = movie_item.xpath('div[@class="info"]/ul[@class="event-meta"]/li[@class="event-time"]/time[@itemprop="startDate"]/@datetime').extract_first()
            movie['endDate'] = movie_item.xpath('div[@class="info"]/ul[@class="event-meta"]/li[@class="event-time"]/time[@itemprop="endDate"]/@datetime').extract_first()
            movie['location'] = movie_item.xpath('div[@class="info"]/ul[@class="event-meta"]/li/@title').extract_first()
            yield movie
            pass

        ##下面的代码应该是个分页的，但是目标网页没有分页的需要！！！！！
        nextPage=response.xpath('//span[@class="next"]/a/@href').extract_first()
        if nextPage:
            url=response.urljoin(nextPage)
            yield  scrapy.Request(url,self.parse)
        pass
