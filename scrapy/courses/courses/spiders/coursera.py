import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    # limita o domínio
    allowed_domains = ['https://www.coursera.org/browse?languages=pt']
    start_urls = ['https://www.coursera.org/browse?languages=pt']

    def parse(self, response):
        self.log('Hello World" Scrapy Project')


