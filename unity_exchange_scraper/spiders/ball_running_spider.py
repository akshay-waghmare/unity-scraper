import scrapy
from scrapy_splash import SplashRequest
import json

class BallRunningSpiderSpider(scrapy.Spider):
    name = "ball_running_spider"

    def start_requests(self):
        # Define API URL, payload, and headers
        
        api_url = 'https://www.unityexch.com/v1/users/userLogin'
        payload = {"userName":"akiaksdon","password":"unityexch1618","ip_info":"{\"ip\":\"103.199.192.50\",\"hostname\":\"AS17665 ONEOTT INTERTAINMENT LIMITED\",\"city\":\"Pune\",\"region\":\"Maharashtra\",\"country\":\"India\",\"loc\":18.6161,\"postal\":\"411001\",\"org\":\"AS17665 ONEOTT INTERTAINMENT LIMITED\"}"}
        payload_bytes = json.dumps(payload).encode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Cookie': '_ga=GA1.1.183286417.1695652252; _ga_DG0Y8CDR0L=GS1.1.1701507880.36.1.1701509435.0.0.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Origin': 'https://www.unityexch.com',
            'Referer': 'https://www.unityexch.com/'
        }

        # Create the Request object with custom headers and payload
        yield scrapy.Request(
            url=api_url,
            method='POST',
            headers=headers,
            body=payload_bytes,  # Convert payload to JSON string
            callback=self.parse_login_response,
        )

    def parse_login_response(self, response):
        # Handle the API response
        login_response = json.loads(response.text)
        print(login_response)
