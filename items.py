# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviesItem(scrapy.Item):
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
