import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from unity_exchange_scraper.spiders.ball_running_spider import BallRunningSpiderSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(BallRunningSpiderSpider)
process.start()