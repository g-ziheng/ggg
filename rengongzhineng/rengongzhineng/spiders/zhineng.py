# -*- coding: utf-8 -*-

import scrapy
import time


class ZhinengSpider(scrapy.Spider):
    name = 'zhineng'
    # allowed_domains = []
    start_urls = ['http://www.ailab.cn/?page=1']

    # rules = (
    #     Rule(LinkExtractor(allow='http://bigdata.ailab.cn/?page=\d+'),follow=True),
    #     Rule(LinkExtractor(allow='http://bigdata.ailab.cn/(.*?).html',restrict_xpaths='//ul[@class="list_jc"]/li/a[1]/@href',),callback='parse_item',follow=False)
    # )

    def parse(self, response):
        # print(response.text)
        url_list = response.xpath('//ul[@class="list_jc"]/li/a[1]/@href').extract()
        for url in url_list:
            # time.sleep(1)
            yield scrapy.Request(url,self.info)

    def info(self,response):
        try:
            # 标题
            title = response.xpath('//div[@class="listltitle"]/h3/text()').extract_first().strip()
            # 时间
            time = response.xpath('//div[@class="listltitle"]/p/span[3]/text()').extract_first().strip()
            # 来源
            if response.xpath('//di                                                                        v[@class="listltitle"]/p/span[2]/text()'):
                laiyuan = response.xpath('//div[@class="listltitle"]/p/span[2]/text()').extract_first()[3:].strip()
            else:
                laiyuan = '来源不明'
            # 关键字
            if response.xpath('//meta[@name="keywords"]/@content'):
                keyword = response.xpath('//meta[@name="keywords"]/@content').extract_first().strip()
            else:
                keyword = '暂无关键字'
            # 导读
            if response.xpath('//meta[@name="description"]/@content'):
                intro = response.xpath('//meta[@name="description"]/@content').extract_first().strip()
            else:
                intro = '暂无导读'
            # 内容
            if response.xpath('//div[@id="mainDiv"]/p/text()'):
                content = ''.join(response.xpath('//div[@id="mainDiv"]/p/text()').extract()).strip()
            else:
                content = '暂无内容'
            # 照片
            if response.xpath('//div[@id="mainDiv"]/center/img/@src'):
                pic = response.xpath('//div[@id="mainDiv"]/center/img/@src').extract()
            else:
                pic = '暂无照片'
        except:
            pass
