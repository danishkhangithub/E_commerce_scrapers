# packages
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import os
import json
import pandas as pd
import csv


# property scraper class
class Amazon(scrapy.Spider):
    # scraper name
    name = 'Amazon'
    allowed_domains = ['amazon.com']
    base_url = 'https://www.amazon.com/'


    # headers
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        }

    file = 'products.xlsx'

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
        'CONCURRENT_REQUEST_PER_DOMAIN': 2,
        'DOWNLOAD_DELAY': 2,
    }

    results = []

    # general crawler
    def start_requests(self):
        url = self.base_url #+ self.tag
        # initial HTTP request
        yield scrapy.Request(
            url=url,
            headers=self.headers,

            callback=self.parse
                  )
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

          product_links = response.css('div[class = "a-section a-spacing-none a-spacing-top-small"] a[class = "a-link-normal"]::attr(href)').getall()[:10]
          try:
            if product_links !=[] or None:
              for link in product_links:
                 links = 'https://www.amazon.com' + link
                 print('\nlinks\n:',links,'\n')
                 yield response.follow(
                         link,
                         headers = self.headers,
                         callback = self.parse_card
                    )
            else:
              print('error\t:', product_links)
              pass
          except Exception as e:
             print('exception:\t\t',e)
             pass



    def parse_card(self, response):
            try:
               name = response.css('span[class= "a-size-large product-title-word-break"]::text').get().strip(),

            except Exception as e:
               print('error\t',e, 'url:\t', response.url)
            items = {
               'Name' : name, #response.xpath('//span[@class = "a-size-large product-title-word-break"]/text()').get().strip(),
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
               Price = 'N/A'

            try:
               Brand =  response.xpath('//th[contains(text(),"Brand")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
               if Brand != '':
                  items['Brand'] = Brand
               else:
                  items['Brand'] = response.xpath('//th[contains(text(),"Brand Name")]').xpath('following-sibling::td/text()').get().strip()

            except:
               Brand = 'N/A'
            try:
               No_of_items = response.xpath('//th[contains(text(),"Number of Items")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
               if No_of_items is not None:
                  items['Number_of_Items'] = No_of_items
               else:
                  Size = response.xpath('//th[contains(text(),"Size")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
                  items['Number_of_Items'] = Size
            except:
               No_of_items = 'N/A'

            try:
               Item_weight = response.xpath('//th[contains(text(),"Item Weight")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
               items['Weight'] = Item_weight
            except Exception as e:
               if e:
                 Item_weight =  response.xpath('//th[contains(text(),"Weight")]').xpath('following-sibling::td/text()').get().strip()
               else:
                   Size = response.xpath('//th[contains(text(),"Size")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
                   items['Weight'] = Size
            try:
               Asin = response.xpath('//th[contains(text(),"ASIN")]').xpath('following-sibling::td/text()').get().strip()
               items['Asin'] = Asin
            except:
               Asin = 'N/A'
            try:

                 Size = response.xpath('//th[contains(text(),"Size")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
                 if Size is not None:
                     items['Size'] = Size
                 size1 = response.xpath('//th[contains(text(),"Size")]').xpath('following-sibling::td/text()').get().strip()
                 elif size1 is not None:
                     items['Size'] = size1
                 else:
                     size2 = response.xpath('//th[contains(text(),"Length")]').xpath('following-sibling::td/text()').get().strip()

                     items['Size'] = size2


            except Exception as e:

               items['Size'] = 'N/A'

            try:
               Item_Model_Number = response.xpath('//th[contains(text(),"Item model number")]').xpath('following-sibling::td/text()').get().strip()
               items['Item_Model_Number'] = Item_Model_Number

            except:
               Item_Model_Number = response.xpath('//th[contains(text(),"Part Number")]').xpath('following-sibling::td/text()').get().strip()


            #yield items
            self.results.append(items)


#            with open('qsranks.csv', 'a') as csv_file:
#                 writer = csv.DictWriter(csv_file, fieldnames=items.keys())
#                 writer.writerow(items)
#


if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(Amazon)
    process.start()
    profile_details = pd.DataFrame(Amazon.results)
    pd.set_option('display.max_columns', None)
    print(profile_details)

    profile_details.to_excel('products2.xlsx')
    print('DataFrame is written to Excel File successfully.')

    #Amazon.parse(Amazon, '')
