# -*- coding: utf-8 -*-
import scrapy

from logocrawl.items import LogoItem
class LogoSpider(scrapy.Spider):
	name = "logo"
	allowed_domains = ["worldvectorlogo.com"]
	URL = "https://worldvectorlogo.com/most-downloaded/"
	start_urls = []
	for i in range(100):
		start_urls.append(URL+str(i+1))

	def parse(self,response):
		for post in response.css('.logo::attr(href)'):
			item = LogoItem()
			item['image'] = post.extract()
			yield item