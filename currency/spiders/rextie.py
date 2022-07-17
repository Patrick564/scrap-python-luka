import scrapy, tempfile
from scrapy.crawler import CrawlerProcess

from datetime import datetime


class RextieSpider(scrapy.Spider):
    name = 'rextie'
    allowed_domains = ['www.rextie.com']
    start_urls = ['http://www.rextie.com/']

    def parse(self, response):
        sell_price = response.xpath("//fx-rates/div/div/div[1]/div[@class='price sell ng-tns-c15-0']/div[@class='amount ng-tns-c15-0']/text()").get()
        buy_price = response.xpath("//fx-rates/div/div/div[1]/div[@class='price buy ng-tns-c15-0']/div[@class='amount ng-tns-c15-0']/text()").get()

        rextie = {
            'sell': sell_price,
            'buy': buy_price,
            'response_time': datetime.now()
        }

        return rextie


if __name__ == '__main__':
    process = CrawlerProcess(settings={
        'FEEDS': {
            f'{tempfile.gettempdir()}/rextie.jsonl': { 'format': 'jsonlines' }
        }
    })

    process.crawl(RextieSpider)
    process.start()
