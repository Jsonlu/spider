#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy

from tutorial.items import DoubanMoviesItem
'''
豆瓣热门电影
'''
class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
    'https://movie.douban.com/cinema/nowplaying/hangzhou/',
    'https://movie.douban.com/cinema/nowplaying/beijing/',
    'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    ]

    def parse(self, response):
        currentpage_movie_items = response.xpath('//li[@class="list-item"]')
        for movie_item in currentpage_movie_items:
            movie = DoubanMoviesItem()
            movie['score'] = movie_item.xpath('@data-score').extract_first()
            movie['title'] = movie_item.xpath('@data-title').extract_first()
            movie['year'] = movie_item.xpath('@data-release').extract_first()
            movie['duration'] = movie_item.xpath('@data-duration').extract_first()
            movie['region'] = movie_item.xpath('@data-region').extract_first()
            movie['director'] = movie_item.xpath('@data-director').extract_first()
            movie['actors'] = movie_item.xpath('@data-actors').extract_first()
            movie['votecount'] = movie_item.xpath('@data-votecount').extract_first()
            movie['pic_url'] = movie_item.xpath('ul/li[@class="poster"]/a/img/@src').extract_first()
            yield movie
            pass
