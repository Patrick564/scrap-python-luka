import scrapy

# from datetime import datetime


class RoblexSpider(scrapy.Spider):
    name = 'roblex'
    allowed_domains = ['roblex.pe']
    start_urls = ['http://roblex.pe/']

    def parse(self, response):
        pass
