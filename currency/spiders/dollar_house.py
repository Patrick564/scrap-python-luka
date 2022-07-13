import scrapy


class DollarHouseSpider(scrapy.Spider):
    name = 'dollar_house'
    allowed_domains = ['app.dollarhouse.pe']
    start_urls = ['http://app.dollarhouse.pe/']

    def parse(self, response):
        sell_price = response.xpath("//span[@id='sell-exchange-rate']/text()").get()
        buy_price = response.xpath("//span[@id='buy-exchange-rate']/text()").get()

        dollar_house = {
            'sell': sell_price,
            'buy': buy_price
        }

        return dollar_house
