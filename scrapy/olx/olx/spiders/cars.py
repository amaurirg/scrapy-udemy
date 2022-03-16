import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['sp.olx.com.br/autos-e-pecas']
    start_urls = ['http://sp.olx.com.br/autos-e-pecas/']

    def parse(self, response):
        items = response.xpath('//ul[@id="ad-list"]/li')
        for item in items:
            self.log(item.xpath('./a/@href').extract_first())

