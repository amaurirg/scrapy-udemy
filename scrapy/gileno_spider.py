import scrapy


class GilenoSpider(scrapy.Spider):
    # nome da spider
    name = 'gilenofilho'
    # lista de urls por onde começará o crawler
    start_urls = ['http://www.gilenofilho.com.br']

    #
    def parse(self, response):
        """
        Quando utilizado start_urls o callback do spider chamará esse parse
        passando a resposta da requisição à página para essa função
        :param response: resposta da requisição para a página
        :return:
        """
        # mostra essa mensagem
        self.log('Hello World')
        # conteúdo da página
        self.log(response.body)


# Rodar spider no terminal
# scrapy runspider gileno_spider.py