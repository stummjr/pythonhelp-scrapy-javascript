import scrapy
from selenium import webdriver


class QuotesSeleniumSpider(scrapy.Spider):
    name = 'quotes-selenium'
    start_urls = ['http://quotes.toscrape.com/js']

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        super(QuotesSeleniumSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # This spider downloads the page twice:
        # - first: the scrapy downloader downloads the page and the parse()
        #   method is called.
        # - second: the get() call below downloads the page again, this time
        #   using selenium
        # We can improve this with a custom middleware, as shown in
        # quotes-selenium-downloader.py and ../middlewares.py
        self.driver.get(response.url)
        sel = scrapy.Selector(text=self.driver.page_source)
        for quote in sel.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }
