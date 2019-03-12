impot scrapy

class MinimalSpider(scrapy.Spider):
    """A menor Scrapy-Aranha do mundo!"""
    nome = 'minimal'
    
    def start_requests(self):
        return (scrapy.Request(url)
                for url in ['http://www.google.com', 'http://www.yahoo.com'])
    def parse(self, response):
        self.log('ACESSANDO URL: %s' % response.url)