# packages
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import json
import csv
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

# hummart spider class
class Amazonspider(scrapy.Spider):
    # scraper / spider name
    name = 'amazon_spider'

    base_url =  'https://www.amazon.com'

    headers = {
      'USER-AGENT' :  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
                    }
    

    
    # custom settings
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'amazon1_3.csv',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'DOWNLOAD_DELAY': 2
       }

    
    # crawler's entry point
    def start_requests(self):
        # make HTTP request to base URL
        yield scrapy.Request(
            url=self.base_url,
            headers=self.headers,
            callback=self.parse_links
        )

    def parse_links(self, res):
           with open('amazon1_2.txt') as f:
             asins = f.read().split('\n')
               
               
           for asin in asins:
               product_url = self.base_url + '/dp/' + asin   
               
               
               yield res.follow(
                            url=product_url,
                            headers=self.headers,
                            callback=self.parse_products
                                 ) 
        
        
        

    def parse_products(self, response):
        '''
        content = ''
        
        # open local HTML file
        with open('amazon3.html', 'r') as f:
            for line in f.read():
                content += line
        
        # init scrapy selector
        response = Selector(text=content)
        '''
        features = {
             
           
             'Shipping_cost' :  response.xpath('//div/table[@class="a-lineitem"]/tbody/tr[2]/td[3]/span/text()').get(),
        
             'Estimated_import_fees'  :  '',      
                }
        
       
        try:
            facts = response.xpath('//div/table[@class="a-lineitem"]/tbody/tr[3]/td[3]/span/text()').get()
            features['Estimated_import_fees'] = facts
           
        except:
           features['Estimated_import_fees'] =  'No Import Fee'
    
        rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths=('//*[@id=""ourprice_shippingmessage"]/SPAN[2]/A',), attrs=('onclick',)))

    )


  
        print(rules)        

if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(Amazonspider)
    process.start()
    #Amazonspider.parse_products(Amazonspider,'')
   
