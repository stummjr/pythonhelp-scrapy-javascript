import scrapy
import js2xml


class QuotesJs2XmlSpider(scrapy.Spider):
    name = 'quotes-js2xml'
    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        script = response.xpath('//script[contains(., "var data =")]/text()').extract_first()
        script_as_xml = js2xml.parse(script)
        sel = scrapy.Selector(_root=script_as_xml)
        for quote in sel.xpath('//var[@name="data"]/array/object'):
            yield {
                'text': quote.xpath('string(./property[@name="text"])').extract_first(),
                'author': quote.xpath(
                    'string(./property[@name="author"]//property[@name="name"])'
                ).extract_first(),
                'tags': quote.xpath('./property[@name="tags"]//string/text()').extract(),
            }
