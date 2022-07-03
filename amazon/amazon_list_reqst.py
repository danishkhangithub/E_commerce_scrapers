# packages
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.utils.response import open_in_browser
import json
import os
import requests
import csv
from scraper import *


# hummart spider class
class Amazonspider(scrapy.Spider):
    # scraper / spider name
    name = 'amazon_spider'

    base_url =  'https://www.amazon.com/s?k=skincare+products&i=beauty&rh=n%3A3760911%2Cn%3A11061121&dc&page=1&crid=2TNB8V67U9FMK&qid=1653478583&rnid=2941120011&sprefix=skincare+products%2Caps%2C481&ref=sr_pg_2'
    headers = {
      'USER-AGENT' :  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
                    }

    results = []

    page = 1

    file = 'amazon_list1.csv'
    try:
       if (os.path.exists(file)) and (os.path.isfile(file)):
          os.remove(file)
       else:
          print('file not found')
    except OSError:
       pass

    # custom settings
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'amazon_list1.csv',
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
        'DOWNLOAD_DELAY': 2,
        'DOWNLOAD_TIMEOUT': 10,
        #'LOG_LEVEL': 'INFO',
       }



    # crawler's entry point
    def start_requests(self):



        # make HTTP request to base URL
        yield scrapy.Request(
            url=self.base_url,
            headers=self.headers,
            callback=self.parse_links
        )


    def parse_links(self, response):

        # next_page = 'https://www.amazon.com/s?k=skincare+products&crid=2TNB8V67U9FMK&sprefix=skincare+products%2Caps%2C481&ref=nb_sb_noss_2'
        for page in range(1,10):
            next_page = 'https://www.amazon.com/s?k=skincare+products&i=beauty&rh=n%3A3760911%2Cn%3A11061121&dc&page='+ str(page)+ '&crid=2TNB8V67U9FMK&qid=1653478583&rnid=2941120011&sprefix=skincare+products%2Caps%2C481&ref=sr_pg_2'
            print(next_page)



            try:
               yield response.follow(
                        url=next_page,
                        headers=self.headers,
                        callback=self.parse_listing,
                        meta = {'page': page,
                                 'dont_redirect': True,
                                'handle_httpstatus_list': [301, 302]},

                            )


               page +=1
            except Exception as e:
                print('\n',e)




    def parse_listing(self, response):
        print(response.meta.get('page'))
        product_urls = response.css('h2 .a-link-normal::attr(href)').getall()
        product_urls = ['https://www.amazon.com' + url for url in product_urls]

        for prod in product_urls:
           response_get = scraper.GET(prod)
           print(response_get, response_get.text)

           parse_products(response_get.text)


#
#            yield response.follow(
#                            url=prod,
#                            headers=self.headers,
#                             dont_filter=True,
#                             meta = {
#                                'dont_redirect': True,
#                                'handle_httpstatus_list': [301, 302]},
#                             callback=self.parse_products
#                                )
#
#

    def parse_products(self, response_get):
        '''
        content = ''

        # open local HTML file
        with open('amazon121.html', 'r') as f:
            for line in f.read():
                content += line

        # init scrapy selector
        response = Selector(text=content)
        '''
        response = Selector(text = response_get)

        #url2 = 'https://www.amazon.com/Wings-Fire-15-Tui-Sutherland/dp/1338214578/ref=sr_1_1?qid=1651656509&s=books&sr=1-1'
#        print(url2.split('dp/')[1].split('/ref')[0])



        Asin = response.url.split('dp/')[1].split('/ref')[0]

        product_details = [i.strip('\n').replace(' ','').replace('\n\u200f\n:\n\u200e\n','') for i in response.css('#detailBullets_feature_div .a-text-bold::text').getall()]

        product_values = response.css('#detailBullets_feature_div .a-text-bold+ span::text').getall()

        product_details2 = {}

        details2 = []

        for index in range(0, len(product_values)):
           product_details2[product_details[index]] = product_values[index]
        for i,v in product_details2.items():
            details = (i,':', v)
            details2.append(details)





        try:
          item_form = response.css('.po-item_form .a-span9 .a-size-base::text').get(),
        except:
          item_form = 'N/A'


        try:
          brand = response.css('.po-brand .a-span9 span::text').get()
        except:
          brand = 'N/A'

        try:
          Produts_benefits = response.css('.a-truncate-cut::text').get()
        except:
          Produts_benefits = 'N/A'


        try:
          Skin_type = response.css('.po-skin_type .a-span9 .a-size-base::text').get()
        except:
          Skin_type = 'N/A'



        try:
          About_the_item =  response.css('#feature-bullets li::text').get(),
        except:
          About_the_item = 'N/A'


        try:
         Recommended_user_for_producr = response.css('.po-recommended_uses_for_product .a-span9 .a-size-base::text').get(),
        except:
          Recommended_user_for_producr = 'N/A'

        try:
          IsDiscontinuedByManufacturer = product_details2['IsDiscontinuedByManufacturer'],
        except:
          IsDiscontinuedByManufacturer = 'N\A'


        try:
          ProductDimensions =  product_details2['ProductDimensions'],
        except:
          ProductDimensions = 'N/A'


        try:
          Reviews = response.css('#acrCustomerReviewText::text').get.strip(' ratings')
        except Exception as e:
          print(e)
          Reviews = 'N/A'
        try:
          Description = response.css('p:nth-child(2) span::text').get(),
        except Exception as e:
          print(e)
          Description = 'N/A'
        try:
          Author = response.css('.notFaded+ .notFaded .a-link-normal::text').get(),
        except Exception as e:
          print(e)
          Author = 'N/A'
        try:
          Safety_Information = response.css('h2+ .content p::text').get(),
        except Exception as e:
          print(e)
          Safety_Information = 'N/A'
        try:
          Indications = response.css('.content:nth-child(3) p::text').get(),
        except Exception as e:
          print(e)
          Indications = 'N/A'
        try:
          Ingredients = response.css('.content:nth-child(4) p::text').get(),
        except Exception as e:
          print(e)
          Ingredients = 'N/A'
        try:
          Directions = response.css('.content:nth-child(5) p::text').get()
        except Exception as e:
          print(e)
          Directions = 'N/A'




        features = {
             'Name' : response.css('#title span[id = "productTitle"]::text').get().strip(),
             'Image' : response.css('div #imgTagWrapperId img::attr(src)').get(),
             'Link' : response.url,
             'ASIN' : Asin,
             'Item_form' : item_form,
             'Brand' : brand,
             'Produts_benefits': Produts_benefits,
             'ProductDimensions': ProductDimensions,
             'Skin_type': Skin_type,
             'About_the_item' : About_the_item,
             'Recommended_user_for_producr' : Recommended_user_for_producr,
             'IsDiscontinuedByManufacturer' : IsDiscontinuedByManufacturer,
             'ProductDimensions' : '',
             'Itemmodelnumber' : '',
             'UPC' : '',
             'Manufacturer': '',
             'Description' : Description, #''.join(response.css('#bookDescription_feature_div .a-text-bold::text').getall()),
             'Author' : Author,
             'Safety_Information' : Safety_Information,
             'Indications' : Indications,
             'Ingredients' : Ingredients,
             #'Details' : details,
             'Reviews' : Reviews,
             'Directions' : Directions

                   }

        try:
             features['ProductDimensions'] = product_details2['ProductDimensions']
        except:
             features['ProductDimensions'] = None

        try:
             features['Itemmodelnumber'] = product_details2['Itemmodelnumber']
        except:
             features['Itemmodelnumber'] = None

        try:
             features['UPC'] = product_details2['UPC']
        except:
             features['UPC'] = None

        try:
             features['Manufacturer'] = product_details2['Manufacturer']
        except:
             features['Manufacturer'] = None


        print(json.dumps(features, indent = 2))



        self.results.append(features)
        headers = features.keys()


        with open('amazon_list1.csv', 'w+', newline = '') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter = ',', fieldnames = headers)
            writer.writeheader()
            writer.writerows(self.results)




if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(Amazonspider)
    process.start()
    # Amazonspider.parse_products(Amazonspider,'')
