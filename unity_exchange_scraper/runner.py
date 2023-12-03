import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.ball_running_spider import BallRunningSpiderSpider

# Set up Scrapy project settings
settings = get_project_settings()

# Additional settings for Scrapy-Splash
settings.set('SPLASH_URL', 'http://localhost:8050')  # Replace with your Splash instance URL
settings.set('DUPEFILTER_CLASS', 'scrapy_splash.SplashAwareDupeFilter')
settings.set('HTTPCACHE_STORAGE', 'scrapy_splash.SplashAwareFSCacheStorage')

process = CrawlerProcess(settings)
process.crawl(BallRunningSpiderSpider)
process.start()