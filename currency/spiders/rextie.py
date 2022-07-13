import scrapy


class RextieSpider(scrapy.Spider):
    name = 'rextie'
    allowed_domains = ['www.rextie.com']
    start_urls = ['http://www.rextie.com/']

    def parse(self, response):
        sell_price = response.xpath("//fx-rates/div/div/div[1]/div[@class='price sell ng-tns-c15-0']/div[@class='amount ng-tns-c15-0']/text()").get()
        buy_price = response.xpath("//fx-rates/div/div/div[1]/div[@class='price buy ng-tns-c15-0']/div[@class='amount ng-tns-c15-0']/text()").get()

        rextie = {
            'sell': sell_price,
            'buy': buy_price
        }

        return rextie