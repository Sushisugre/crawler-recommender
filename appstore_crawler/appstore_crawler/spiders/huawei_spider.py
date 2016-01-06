import scrapy
import re
from scrapy.selector import Selector
from appstore_crawler.items  import AppstoreCrawlerItem

class HuaweiSpider(scrapy.Spider):
    name = "huawei"
    allowed_domains = ["huawei.com"]

    start_urls = [
        "http://appstore.huawei.com/more/all"
    ]

    """
        Get app detail from homepage, and craw the app detail page
    """
    def parse(self, response):
        page = Selector(response)
        hrefs = page.xpath('//h4[@class="title"]/a/@href')

        for href in hrefs:
            url = href.extract()
            # yield scrapy.Request(url, callback = self.parse_item)
            yield scrapy.Request(url, self.parse_item, meta={
                'splash': {
                    'endpoint' : 'render.html',
                    'args' : {'wait': 0.5}
                }
            })

    """
        Extract information for app detail page
    """
    def parse_item(self, response):
        page = Selector(response)
        item = AppstoreCrawlerItem()
        item['title'] = page.xpath('//ul[@class="app-info-ul nofloat"]/li/p/span[@class="title"]/text()'). \
            extract_first().encode('utf-8')
        item['thumbnail'] = page.xpath('//ul[@class="app-info-ul nofloat"]/li/img[@class="app-ico"]/@src').extract_first()
        item['url'] = response.url
        appid = re.match(r'http://.*/(.*)', item['url']).group(1)
        item['appid'] = appid
        item['intro'] = page.xpath('//meta[@name="description"]/@content'). \
            extract_first().encode('utf-8')

        divs = page.xpath('//div[@class="open-info"]')
        recomm = ""
        for div in divs:
            url = div.xpath('./p[@class="name"]/a/@href').extract_first()
            recommended_appid = re.match(r'http://.*/(.*)', url).group(1)
            name = div.xpath('./p[@class="name"]/a/text()').extract_first().encode('utf-8') 
            recomm += "{0}:{1},".format(recommended_appid, name)

        item['recommended'] = recomm
        yield item
