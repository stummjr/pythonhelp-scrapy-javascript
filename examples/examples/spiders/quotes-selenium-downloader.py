import scrapy


# This spider is using the SeleniumDownloader to fetch the pages transparently.
# Check the middleware at ..middlewares.SeleniumDownloader
class QuotesSeleniumDownloaderSpider(scrapy.Spider):
    name = 'quotes-selenium-downloader'
    start_urls = ['http://quotes.toscrape.com/js']
    custom_settings = {
        'SELENIUM_DOWNLOADER_ENABLED': True
    }

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
            # To disable Selenium for a specific request, just pass a meta argument:
            # yield scrapy.Request(response.urljoin(next_page_url), meta={'nojs': 1})
