#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy

from tutorial.items import TaoBaoMMItem

class TaoBaoMMSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["mm.taobao.com"]
    start_urls = ['https://mm.taobao.com/search_tstar_model.htm']

    def parse(self, response):
        currentpage_movie_items = response.xpath('//li[@class="item"]')
        for movie_item in currentpage_movie_items:
            movie = TaoBaoMMItem()
            movie['img'] = movie_item.xpath('div[@class="item-wrap"]/div[@class="img"]/img/@src').extract_first()
            yield movie
            pass
        '''
        ##下面的代码应该是个分页的，但是目标网页没有分页的需要！！！！！
        nextPage=response.xpath('//span[@class="next"]/a/@href')
        if nextPage:
            url=response.urljoin(nextPage[0].extract())
            yield  scrapy.Request(url,self.parse)
        pass
        '''
