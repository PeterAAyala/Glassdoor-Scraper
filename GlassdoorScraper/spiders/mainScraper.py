# -*- coding: utf-8 -*-
import scrapy
from GlassdoorScraper.items import GlassdoorscraperItem


class MainscraperSpider(scrapy.Spider):
    name = 'mainScraper'
    allowed_domains = ['www.glassdoor.com']
    start_urls = ['https://www.glassdoor.com/Reviews/Dialexa-Reviews-E791734.htm']


    def parse(self, response):
        for item in self.scrape(response):
            yield item

        nextpageurl = response.xpath("//a[@class='pagination__ArrowStyle__nextArrow  ']/@href").extract_first()

        if nextpageurl:
            nextpage = response.urljoin(nextpageurl)
            print("Found url: {}".format(nextpage))
            yield scrapy.Request(nextpage, callback = self.parse)

    def scrape(self, response):
        for resource in response.xpath("//div[@class = 'hreview']/.."):
            
            item = GlassdoorscraperItem()

            item['date'] = resource.xpath('descendant::time[@class = "date subtle small"]/text()').extract_first()
            item['OverallRating'] = resource.xpath("descendant::span[@class = 'value-title']/@title").extract_first()
            item['Title'] = resource.xpath('descendant::a[@class = "reviewLink"]/text()').extract_first()

            item['Worklife'] = self.subratingsScraper(formType = "Work/Life Balance", resource = resource)
            item['CareerOps'] = self.subratingsScraper(formType = "Career Opportunities", resource = resource)
            item['Compensation'] = self.subratingsScraper(formType = "Compensation and Benefits", resource = resource)
            item['SeniorManagement'] = self.subratingsScraper(formType = "Senior Management", resource = resource)
            item['CultureValues'] = self.subratingsScraper(formType = "Culture & Values", resource = resource)

            item['Pros'] = self.textScraper(formType = "Pros", resource = resource)
            item['Cons'] = self.textScraper(formType = "Cons", resource = resource)
            item['Feedback'] = self.textScraper(formType = "Advice to Management", resource = resource)

            item['CEO_Opinion'] = self.otherScraper(formType = "CEO", resource = resource)
            item['Recommendation'] = self.otherScraper(formType = "Recommend", resource = resource)
            item['Outlook'] = self.otherScraper(formType = "Outlook", resource = resource)

            yield item

    def textScraper(self, formType, resource):
        # Make sure to include the quotations around the formType
        path = 'descendant::p[text() ="' + formType + '"]/following-sibling::p'
        hiddenText = '/span[@class = "d-none"]/text()'
        if resource.xpath(path + hiddenText).extract_first():
            return resource.xpath(path + '/text()').extract_first()[:-3] + resource.xpath(path + hiddenText).extract_first()
        else: 
            return resource.xpath(path + '/text()').extract_first()
    
    def subratingsScraper(self, formType, resource):    
        path = 'descendant::ul/li/div[text() = "' + formType + '"]/following-sibling::span/@title'
        return resource.xpath(path).extract_first()

    def otherScraper(self, formType, resource):
        path = 'descendant::div[@class = "row reviewBodyCell recommends"]/div/span[contains(text(),"' + formType + '")]/text()'
        return resource.xpath(path).extract_first()


            