import scrapy
from scrapy.crawler import CrawlerProcess

from datetime import datetime


class DollarHouseSpider(scrapy.Spider):
    name = 'dollar_house'
    allowed_domains = ['app.dollarhouse.pe']
    start_urls = ['http://app.dollarhouse.pe/']

    def parse(self, response):
        sell_price = response.xpath("//span[@id='sell-exchange-rate']/text()").get()
        buy_price = response.xpath("//span[@id='buy-exchange-rate']/text()").get()

        dollar_house = {
            'sell': sell_price,
            'buy': buy_price,
            'response_time': datetime.now()
        }

        return dollar_house


if __name__ == '__main__':
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'cambi.jsonl'
    })

    process.crawl(DollarHouseSpider)
    process.start()
