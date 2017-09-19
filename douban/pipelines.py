# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient
from scrapy.conf import settings


class DoubanPipeline(object):

    def __init__(self):
        self.file = open('douban.csv', 'w')

    def process_item(self, item, spider):
        result = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(result)
        return item

    def close_spride(self):
        self.file.close()


class MonogoDBPipeline(object):

    def __init__(self):

        host = settings['MONOGO_HOST']
        port = settings['MONOGO_PORT']
        data = settings['MONOGO_DATA']
        col = settings['MONOGO_CLINE']

        self.heander = MongoClient(host, port)
        self.database = self.heander[data]
        self.cline = self.database[col]

    def process_item(self, item, spider):
        datab = dict(item)
        self.cline.insert(datab)
        return item

    def close_spider(self):
        self.heander.close()
