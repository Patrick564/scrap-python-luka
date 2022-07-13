import scrapy, re


class InkaMoneySpider(scrapy.Spider):
    name = 'inka_money'
    allowed_domains = ['www.inkamoney.com']
    start_urls = ['http://www.inkamoney.com/']

    def parse(self, response):
        primary_div = response.xpath("//div[@class='banner__primary-right']/inka-conversor-home").get()
        extract_price = re.findall('[0-9].[0-9]*', primary_div)

        inka_money = {
            'sell': extract_price[1],
            'buy': extract_price[0]
        }

        return inka_money
