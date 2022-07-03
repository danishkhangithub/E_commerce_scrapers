import scrapy
from scrapy.crawler import CrawlerProcess


class TestSpider(scrapy.Spider):
    name = "test"

    start_urls = [
        "https://www.amazon.com/Diamond-Square-Sterling-Silver-Size-7/dp/B0773P8G97/ref=pd_di_sccai_2/136-2464159-4638640?pd_rd_w=Wuofp&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=M7QXR6MRX6X26XRG0RQC&pd_rd_r=eed9c9b9-8df2-4e08-9623-286997495721&pd_rd_wg=muoB4&pd_rd_i=B0773P8G97&th=1&psc=1",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)


if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
    #Amazonspider.parse_products(Amazonspider,'')
