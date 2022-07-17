import scrapy, re, tempfile
from scrapy.crawler import CrawlerProcess

from datetime import datetime


class InkaMoneySpider(scrapy.Spider):
    name = 'inka_money'
    allowed_domains = ['www.inkamoney.com']
    start_urls = ['http://www.inkamoney.com/']

    def parse(self, response):
        primary_div = response.xpath("//div[@class='banner__primary-right']/inka-conversor-home").get()
        extract_price = re.findall('[0-9].[0-9]*', primary_div)

        inka_money = {
            'sell': extract_price[1],
            'buy': extract_price[0],
            'response_time': datetime.now()
        }

        return inka_money


if __name__ == '__main__':
    process = CrawlerProcess(settings={
        'FEEDS': {
            f'{tempfile.gettempdir()}/inka_money.jsonl': { 'format': 'jsonlines' }
        }
    })

    process.crawl(InkaMoneySpider)
    process.start()
