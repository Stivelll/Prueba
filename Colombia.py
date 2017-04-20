from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class AirbnbItem(Item):
	titulo = Field()
	texto = Field()
	url = Field()
	
class AirbnbCrawler(CrawlSpider):
		name= "Spider"
		start_urls= [
			"http://www.colombia.com/turismo/" 
			]
		allowed_domains= [		
			"colombia.com"
		]
		
		rules= {
			Rule(LinkExtractor(allow=r'/turismo'), callback = 'parse_items'),
		}
		def parse_items(self, response):
			item = ItemLoader(AirbnbItem(), response)
			item.add_value('url', response.url)
			item.add_xpath('titulo', '/html/body/div[2]/div[2]/div/div[7]/div[1]/div/article/div[2]/h1/text()')
			item.add_xpath('texto', str.replace('.//p/text()', ""))
			item.add_xpath('texto', './/p/strong/text()')
			yield item.load_item()
