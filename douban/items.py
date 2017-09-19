# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # 电影名称
    name = scrapy.Field()
    # 影片评分
    souce = scrapy.Field()
    # 影片介绍
    info = scrapy.Field()
    # 影片信息
    count  = scrapy.Field()
    # 影片内容
    # propery = scrapy.Field()
