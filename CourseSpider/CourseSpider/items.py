# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Course(scrapy.Item):
    title = scrapy.Field()
    subtitle = scrapy.Field()
    about = scrapy.Field()

    cover = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    
    rating = scrapy.Field()
    ratingN = scrapy.Field()
    hitN = scrapy.Field()

    #N普通/L直播/V视频/C班级/O公开课
    ctype = scrapy.Field()
    site = scrapy.Field()
    tags = scrapy.Field()

    updated = scrapy.Field()

    #out
    o_price = scrapy.Field()
    o_rating = scrapy.Field()
    o_ratingN = scrapy.Field()
    o_stuN = scrapy.Field()
    o_reviewN = scrapy.Field() #评论数
    o_hitN = scrapy.Field() #点击数

    #adm
    adm_rating = scrapy.Field()