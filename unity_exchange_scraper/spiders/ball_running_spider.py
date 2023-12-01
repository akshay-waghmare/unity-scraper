import scrapy


class BallRunningSpiderSpider(scrapy.Spider):
    name = "ball_running_spider"
    allowed_domains = ["unity-exchange-website.com"]
    start_urls = ["http://unity-exchange-website.com/"]

    def parse(self, response):
        pass
