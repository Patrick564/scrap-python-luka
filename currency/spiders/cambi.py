import scrapy
from scrapy.crawler import CrawlerProcess

from datetime import datetime


class CambiSpider(scrapy.Spider):
    name = 'cambi'
    allowed_domains = ['www.cambi.pe']
    start_urls = ['http://www.cambi.pe/']

    def parse(self, response):
        extract_price = response.xpath("//div[@class='tipo_cambio']/span/strong/text()").extract()

        cambi = {
            'sell': extract_price[1],
            'buy': extract_price[0],
            'response_time': datetime.now()
        }

        return cambi


if __name__ == '__main__':
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'cambi.jsonl'
    })

    process.crawl(CambiSpider)
    process.start()
