import scrapy,string
from tutorial.items import DomzItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["man.lv"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "http://cl.man.lv/thread0806.php?fid=15"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath("//tr/td[@style='text-align:left;padding-left:8px']"):
            baseList = ['http://cl.man.lv/']
            item = DomzItem()
            # item['title'] = sel.xpath('a/text()').extract()
            item['links'] = sel.xpath("h3/a[@target='_blank']/@href").extract()
            # item['links'] = baseList.extend(item.get('links'))
            # item['desc'] = sel.xpath('text()').extract()
            baseList.extend(item['links']);
            item['links'] = string.join(baseList,'')

            yield item
