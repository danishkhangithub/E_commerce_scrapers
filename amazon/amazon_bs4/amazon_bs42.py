# packages

from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import requests
from bs4 import BeautifulSoup

class Amazon():
    url = 'https://www.amazon.com'
    def scrape(self):

        r = requests.get(self.url)

        response = Selector(text = r.text)


        categories =  response.xpath('//select[@id = "searchDropdownBox"]/option/@value').extract()[1:11]
        print(categories)
        for cat in categories:
            cat_url = 'https://www.amazon.com/s/ref=nb_sb_noss?' + cat
            print(cat_url)

#            r = requests.get(cat_url)
#
#            res = Selector(text = r.text)
#
#            product_links = res.css('div[class = "a-section a-spacing-none a-spacing-top-small"] a[class = "a-link-normal"]::attr(href)').getall()[:5]
#            #if product_links !=[]:
#            print(product_links)

#          try:
#             for link in product_links:
#                links = 'https://www.amazon.com' + link
#                print('\nlinks\n:',links,'\n')
#
#                r = requests.get(links)
#                card = Selector(text = r.text)
#                print(card)
#          else:
#            print('error\t:', product_links)
#            pass
#
#
#
#            items = {
#               'Name' : response.xpath('//span[@class = "a-size-large product-title-word-break"]/text()').get().strip(),
#               'Price' : '',
#               'Brand' : '',
#               'No_Of_Items' : '',
#               'Weight' : '',
#               'Asin' : '',
#               'Reviews' :response.xpath('//th[contains(text(),"Customer Reviews")]').xpath('following-sibling::td//a/span/text()').get(),
#               'Size' :  '',
#               'Item_Model_Number' : '',
#
#
#            }
#
#
#            try:
#               Price = response.css('span[id = "priceblock_ourprice"]::text').get().strip()
#               items['Price'] = Price
#            except:
#               Price = 'Currently_not_available'
#
#            try:
#               Brand =  response.xpath('//th[contains(text(),"Brand")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
#
#               items['Brand'] = Brand
#
#
#            except:
#               Brand = 'Not_Known'
#            try:
#               No_of_items = response.xpath('//th[contains(text(),"Number of Items")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
#               items['Number_of_Items'] = No_of_items
#            except:
#               No_of_items = 'Not_Known'
#
#            try:
#               Item_weight = response.xpath('//th[contains(text(),"Item Weight")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
#               items['Weight'] = Item_weight
#            except:
#               Item_weight =  'Not_available'#response.xpath('//th[contains(text(),"Item Weight")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[0].strip()
#
#            try:
#               Asin = response.xpath('//th[contains(text(),"ASIN")]').xpath('following-sibling::td/text()').get().strip()
#               items['Asin'] = Asin
#            except:
#               Asin = 'Not_available'
#            try:
#               Size = response.xpath('//th[contains(text(),"Size")]').xpath('following-sibling::td/text()').get().split('\n\u200e')[1].strip()
#               items['Size'] = Size
#               #Weight = response.xpath('//th[contains(text(),"Weight")]').xpath('following-sibling::td/text()').get().strip()
#            except:
#               Size = 'Not_available'
#
#            try:
#               Item_Model_Number = response.xpath('//th[contains(text(),"Item model number")]').xpath('following-sibling::td/text()').get().strip()
#               items['Item_Model_Number'] = Item_Model_Number
#            except:
#               Item_Model_Number = 'Not_available'
#
#
#
#            self.results.append(items)
#
#    #        with open('products.csv', 'w', newline='', encoding='utf-8') as f:
#    #            writer = csv.DictWriter(f,
#    #                                    fieldnames=['Name', 'Brand', 'Price','No_Of_Items', 'Weight','Asin','Reviews','Size', 'Item_Model_Number'])
#    #            writer.writeheader()
#    #            writer.writerows(self.results)
#
#            with open('qsranks.csv', 'w') as csv_file:
#                 writer = csv.DictWriter(csv_file, fieldnames=items.keys())
#                 writer.writerows(items)
#

if __name__ == '__main__':
    scraper = Amazon()
    scraper.scrape()
