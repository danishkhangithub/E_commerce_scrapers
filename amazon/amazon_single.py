# packages
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import json
import csv
import os

# hummart spider class
class Amazonspider(scrapy.Spider):
    # scraper / spider name
    name = 'amazon_spider'

    base_url =  'https://www.amazon.com/Harry-Potter-Order-Phoenix-Book/dp/043935806X/'
    headers = {
      'USER-AGENT' :  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
                     }
    file = 'amazon_single111.csv'
    try:
       if (os.path.exists(file)) and (os.path.isfile(file)):
          os.remove(file)
       else:
          print('file not found')
    except OSError:
       pass

    results = []

    # custom settings
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'amazon1.csv',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'DOWNLOAD_DELAY': 2
       }


    # crawler's entry point
    def start_requests(self):
        # make HTTP request to base URL
        yield scrapy.Request(
            url=self.base_url,
            headers=self.headers,
            callback=self.parse_products
        )



    def parse_products(self, response):

        content = ''

        # open local HTML file
        with open('amazon111.html', 'r') as f:
            for line in f.read():
                content += line

        # init scrapy selector
        response = Selector(text=content)

        product_details = [i.strip('\n').replace(' ','').replace('\n\u200f\n:\n\u200e\n','') for i in response.css('#detailBullets_feature_div .a-text-bold::text').getall()]

        product_values = response.css('#detailBullets_feature_div .a-text-bold+ span::text').getall()

        product_details2 = {}

        details2 = []

        for index in range(0, len(product_values)):
           product_details2[product_details[index]] = product_values[index]
        for i,v in product_details2.items():
            details = (i,':', v)
            details2.append(details)

        print(details2)

        features = {
             'Name' : response.css('#productTitle::text').get().strip(),
             'Image' : response.css('#imgTagWrapperId img::attr(src)').get(),
             'Item_form' : response.css('.po-item_form .a-span9 .a-size-base::text').get(),
             'ASIN' : product_details2['ASIN'],
             'Brand' : response.css('.po-brand .a-span9::text').get(),
             'Produts_benefits' : response.css('.a-truncate-cut::text').get(),
             'Skin_type' : response.css('.po-skin_type .a-span9 .a-size-base::text').get(),
             'About_the_item' : response.css('#feature-bullets li::text').get(),
             'Recommended_user_for_producr' : response.css('.po-recommended_uses_for_product .a-span9 .a-size-base::text').get(),
             'IsDiscontinuedByManufacturer' : product_details2['IsDiscontinuedByManufacturer'],
             'ProductDimensions' : product_details2['ProductDimensions'],
             'Itemmodelnumber' : product_details2['Itemmodelnumber'],
             'UPC' : product_details2['UPC'],
             'Manufacturer': product_details2['Manufacturer'],
             'Reviews' : response.css('#acrCustomerReviewText::text').get(),
             'Description' : response.css('p:nth-child(2) span::text').get(),
             'Author' : response.css('.notFaded+ .notFaded .a-link-normal::text').get(),
             'Safety Information' : response.css('h2+ .content p::text').get(),
             'Indications' : response.css('.content:nth-child(3) p::text').get(),
             'Ingredients' : response.css('.content:nth-child(4) p::text').get(),
             'Directions' : response.css('.content:nth-child(5) p::text').get()

                   }

        print(features)

        self.results.append(features)
        headers = features.keys()

        with open('amazon_single111.csv', 'w+', newline = '') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter = ',', fieldnames = headers)
            writer.writeheader()
            writer.writerows(self.results)

if __name__ == '__main__':
    # run scraper
#    process = CrawlerProcess()
#    process.crawl(Amazonspider)
#    process.start()
    Amazonspider.parse_products(Amazonspider,'')
