import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['https://br.udacity.com/courses/all//']

    def parse(self, response):
        pass
 