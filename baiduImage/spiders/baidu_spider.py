# coding=utf-8
import scrapy
import json
from baiduImage.items import BaiduimageItem


class Meinv(scrapy.Spider):
    name = 'Meinv'
    start_urls = [
    'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=刘旭阳&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=刘旭阳&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=%d' %i for i in range(0,451,30)
    ]

    def parse(self, response):
        imgs = json.loads(response.body)['data']
        for img in imgs:
            item = BaiduimageItem()
            try:
                item['IMG_URL'] = [img['middleURL']]
                yield item
            except Exception as e:
                print e