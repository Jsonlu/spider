# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    score = scrapy.Field()
    title = scrapy.Field()
    pic_url = scrapy.Field()
    year = scrapy.Field()
    star = scrapy.Field()
    duration = scrapy.Field()
    region = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    votecount = scrapy.Field()
    pass

class TuiCoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    tip = scrapy.Field()
    desc = scrapy.Field()
    pass


class EventItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    location = scrapy.Field()
    startDate = scrapy.Field()
    endDate = scrapy.Field()
    pass


class AliPayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    time = scrapy.Field()
    info = scrapy.Field()
    amountIncome = scrapy.Field()
    amountOutlay = scrapy.Field()
    balance = scrapy.Field()
    detail = scrapy.Field()
    fromAddr = scrapy.Field()
    pass

# link title outline time pic_url
class PaynewsItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    outline = scrapy.Field()
    time = scrapy.Field()
    pic_url = scrapy.Field()
    pass




class ApplyCarItem(scrapy.Item):
    no = scrapy.Field()
    name = scrapy.Field()
    month = scrapy.Field()
    pass
