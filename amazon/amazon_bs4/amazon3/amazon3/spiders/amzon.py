import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import os
import urllib
import json
import datetime
import pandas as pd
import csv

class AmzonSpider(scrapy.Spider):
    name = 'amzon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    # headers
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }

    file = 'propertyfinder.csv'

    try:
      if(os.path.exists(file) and os.path.isfile(file)):
         os.remove(file)
         print('file deleted')
      else:
         print('file not found')
    except OSError:
       pass

    # custom settings
    custom_settings = {
        'CONCURRENT_REQUEST_PER_DOMAIN': 3,
        'DOWNLOAD_DELAY': 1,
        #'FEED_FORMAT': 'csv',
        #'FEED_URI': 'propertyfinder.csv'
    }

    results = []

    def __init__(self):
       pass


    def parse(self, response):

        categories =  response.xpath('//select[@id = "searchDropdownBox"]/option/@value').extract()[1:20]
        for cat in categories:
            cat_url = 'https://www.amazon.com/s/ref=nb_sb_noss?' + cat

            yield response.follow(
               url = cat_url,
               headers = self.headers,
               callback = self.parse_links
             )
        #break

    def parse_links(self, response):

        product_links = response.css('div[class = "a-section a-spacing-none a-spacing-top-small"] a[class = "a-link-normal"]::attr(href)').getall()[:5]

        try:
             links = 'https://www.amazon.com' + urllib.urlencode(link)
             print('\nlinks\n:',links,'\n')

             yield response.follow(
                     url = links,
                     headers = self.headers,
                     callback = self.parse_card
                )
        except:
          print('error\t:', product_links)
          pass




    def parse_card(self, response):

            items = {
               'Name' : response.xpath('//span[@class = "a-size-large product-title-word-break"]/text()').get().strip(),
               'Price' : '',
               'Brand' : '',
               'No_Of_Items' : '',
               'Weight' : '',
               'Asin' : '',
               'Reviews' :response.xpath('//th[contains(text(),"Customer Reviews")]').xpath('following-sibling::td//a/span/text()').get(),
               'Size' :  '',
               'Item_Model_Number' : '',


            }


            try:
               Price = response.css('span[id = "priceblock_ourprice"]::text').get().strip()
               items['Price'] = Price
            except:
               Price = 'Currently_not_available'

            try:
               Brand =  response.xpath('//th[contains(text(),"Brand")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
               items['Brand'] = Brand
            except:
               Brand = 'Not_Known'
            try:
               No_of_items = response.xpath('//th[contains(text(),"Number of Items")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
               items['Number_of_Items'] = No_of_items
            except:
               No_of_items = 'Not_Known'

            try:
               Item_weight = response.xpath('//th[contains(text(),"Item Weight")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
               items['Weight'] = Item_weight
            except:
               Item_weight =  'Not_available'#response.xpath('//th[contains(text(),"Item Weight")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[0].strip()

            try:
               Asin = response.xpath('//th[contains(text(),"ASIN")]').xpath('following-sibling::td/text()').get().strip()
               items['Asin'] = Asin
            except:
               Asin = 'Not_available'
            try:
               Size = response.xpath('//th[contains(text(),"Size")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
               items['Size'] = Size
               #Weight = response.xpath('//th[contains(text(),"Weight")]').xpath('following-sibling::td/text()').get().strip()
            except:
               Size = 'Not_available'

            try:
               Item_Model_Number = response.xpath('//th[contains(text(),"Item model number")]').xpath('following-sibling::td/text()').get().strip()
               items['Item_Model_Number'] = Item_Model_Number
            except:
               Item_Model_Number = 'Not_available'


            yield items
            self.results.append(items)


profile_details = pd.DataFrame(AmzonSpider.results)
pd.set_option('display.max_columns', None)
print(profile_details)

profile_details.to_excel('products2.xlsx')
print('DataFrame is written to Excel File successfully.')
    #        with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    #            writer = csv.DictWriter(f,
    #                                    fieldnames=['Name', 'Brand', 'Price','No_Of_Items', 'Weight','Asin','Reviews','Size', 'Item_Model_Number'])
    #            writer.writeheader()
    #            writer.writerows(self.results)

#            with open('qsranks.csv', 'a') as csv_file:
#                 writer = csv.DictWriter(csv_file, fieldnames=items.keys())
#                 writer.writerow(items)
#
