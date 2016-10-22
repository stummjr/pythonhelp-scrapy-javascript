# -*- coding: utf-8 -*-

BOT_NAME = 'examples'

SPIDER_MODULES = ['examples.spiders']
NEWSPIDER_MODULE = 'examples.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'examples.middlewares.SeleniumDownloader': 543,
}
