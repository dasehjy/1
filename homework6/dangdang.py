import scrapy
import json
from scrapy import Selector

from spider1.items import Goods

class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["e.dangdang.com"]
    # start_urls = ["https://e.dangdang.com/classification_list_page.html?category=JSJWL&dimension=dd_sale&order=0"]
    start_urls = ["https://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20231106125943234417860143002793757&returnType=json&channelId=70000&clientVersionNo=6.8.0&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start=0&end=1000&category=JSJWL&dimension=dd_sale"]

    def parse(self, response):
        res = json.loads(response.text)
        print(len(res['data']['saleList']))
        saleList = res['data']['saleList']
        for sale in saleList:
            mediaList = sale['mediaList']
            for media in mediaList:
                book = Goods()
                book['title'] = media['title']
                book['author'] = media['authorPenname']
                book['introduction'] = media['descs']
                book['price'] = media['price'] / 100
                yield book