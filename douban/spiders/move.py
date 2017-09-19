# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from douban.items import DoubanItem


class MoveSpider(CrawlSpider):
    name = 'move'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    print(start_urls)

    rules = (
        # 匹配每一页的ＵＲＬ
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/\d+/'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        # print(response)
        node_list = response.xpath('//div/div[1]/ol/li/div/div[2]')
        print("=========================================")
        print(len(node_list))
        item = DoubanItem()
        for node in node_list:
            # 取影片名字
            item['name'] = node.xpath("./div[1]/a/span/text()").extract_first()
            # 取影片的评分
            item['souce'] = node.xpath('./div[2]/div/span[2]/text()').extract_first()
            # 取影片信息
            item['info'] = ''.join([i.strip() for i in node.xpath('./div[2]/p[1]/text()').extract()]).replace('\xa0', '')
            # 取影片的内容
            item['info'] = node.xpath("./div[2]/p[2]/span/text()").extract()
            # 详情页面的内容
            # item['propery'] = response.xpath('//*[@id="link-report"]uanzhi302/span[1]/text()').extract()
            yield item

