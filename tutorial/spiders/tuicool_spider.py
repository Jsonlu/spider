#_*_encoding:utf-8 _*_
__author__='JsonLu'
__date__='2018/5/11'

import scrapy
from tutorial.items import TuiCoolItem

'''
推酷推荐
需要推酷登录后的cookie
'''
class TuicoolSpider(scrapy.Spider):
    name = "tuicool"
    allowed_domains = ["tuicool.com"]
    start_urls = ['https://www.tuicool.com/a/']

    cookie = {'_tuicool_session':'BAh7C0kiD3Nlc3Npb25faWQGOgZFRkkiJWRmNTlmN2U4NzdkMDkwNjM3OTQ4NTJkMWZiZDhhMTAyBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVFJRlBKWWZka3hhemxucmVoSlpUU3pXb0xwY0ExNnpPT3BuS0h6ZDNFVzg9BjsARkkiDHVzZXJfaWQGOwBGaQMuiAJJIg51c2VyX2NpdHkGOwBGSSIL5YWo5Zu9BjsAVEkiE3VzZXJfY2l0eV9jb2RlBjsARkkiCGFsbAY7AFRJIg5yZXR1cm5fdG8GOwBGSSItaHR0cHM6Ly93d3cudHVpY29vbC5jb20vYXJ0aWNsZXMvWlpOVkJ6egY7AFQ%3D--7bc9163802b1d3bec3de78460bc87564940453bb'}

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

        nextPage=response.xpath('//li[@class="next"]/a/@href').extract_first()
        if nextPage:
            url = response.urljoin(nextPage)
            yield  scrapy.Request(url,self.parse)
        pass
