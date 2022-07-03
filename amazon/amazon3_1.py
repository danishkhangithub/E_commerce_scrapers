# packages
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import json
import csv

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
        'FEED_URI': 'amazon1_4.csv',
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
           #with open('amazon1_2.txt') as f:
           #  asins = f.read().split('\n')
               
               
           #for asin in asins:
           product_url = self.base_url + 's?k=' + str(887961860221)   
               
               
           yield res.follow(
                        url=product_url,
                        headers=self.headers,
                        callback=self.parse_products
                            ) 
        
        
        

    def parse_products(self, response):
        
        #content = ''
        
        # open local HTML file
        #with open('amazon3.html', 'r') as f:
        #    for line in f.read():
        #        content += line
        
        # init scrapy selector
        #response = Selector(text=content)
        
        print('ok')
        '''
        features = {
             
           
             'Product_Name' : response.css('span[class= "a-size-large product-title-word-break"]::text')
                              .get()
                              .replace('\n',''),
             'Category'  : response.css('span[class="a-list-item"]')
                                  .css('a::text').getall()[3].replace('\n', '').strip(),  
           
             'Price' : response.css('span[class= "a-size-medium a-color-price priceBlockBuyingPriceString"]::text')
                              .get(),

             'Stock' : response.css('span[class="a-dropdown-container"]')
                               .css('select[name="quantity"]')
                               .css('option::text').getall()[-1].strip('\n'), 
            
             'Reviews' : response.css('i[class= "a-icon a-icon-star a-star-4-5"]')
                                     .css('span[class="a-icon-alt"]::text')
                                     .get(),
             'Rank_1'  :   ''.join([rank.get().strip('\n('')') for rank in response.xpath('//*[@class="a-section feature detail-bullets-wrapper bucket"]/ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"]/li /span[@class="a-list-item"]/text()')]), 
             'Rank_2'  : '',                                   

         

             'Image_url'  : response.css('div[class="imgTagWrapper"]').css('img::attr(src)').get(),       

            
       
                }
        print(features)
        '''
        #rank_2 =  ''.join([rank.get() for rank in response.xpath('//*[@class="a-section feature detail-bullets-wrapper bucket"]/ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"]/li/span[@class="a-list-item"]/ul/li/span/text()')]),         

        #features['Rank_2'] = rank_2 +  ''.join([rank.get() for rank in response.xpath('//*[@class="a-section feature detail-bullets-wrapper bucket"]/ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"]/li/span[@class="a-list-item"]/ul/li/span/a/text()')])                                      

        

if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(Amazonspider)
    process.start()
    #Amazonspider.parse_products(Amazonspider,'')
   
