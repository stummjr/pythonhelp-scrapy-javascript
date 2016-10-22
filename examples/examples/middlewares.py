from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.exceptions import NotConfigured
import selenium.webdriver as webdriver


class SeleniumDownloader(object):

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    @classmethod
    def from_crawler(cls, crawler):
        o = cls()
        if not crawler.settings.getbool('SELENIUM_DOWNLOADER_ENABLED'):
            raise NotConfigured
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

    def process_request(self, request, spider):
        if 'nojs' in request.meta:
            return
        self.driver.get(request.url)
        content = self.driver.page_source.encode('utf-8')
        return HtmlResponse(request.url, body=content)

    def spider_closed(self, spider):
        self.driver.close()
