import scrapy
from urllib.parse import urljoin
import csv

from scrapy.http import Response

class EciSpider(scrapy.Spider):
    name='adit'
    allowed_domains = ['https://result.eci.gov.in/']
    start_urls = ["https://results.eci.gov.in/PcResultGenJune2024/index.htm"]
    count=0
    custom_settings = {
        'DOWNLOAD_DELAY':1
    }
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url= url,callback=self.parse , dont_filter=True)
            
            
    def parse(self, response):
        party_urls = response.xpath('//table[@class="table"]/tbody/tr/td[2]/a/@href').getall()
        
        for party_url in party_urls:
            absoulte_party_url = urljoin(response.url,party_url)
            yield scrapy.Request(absoulte_party_url,callback=self.parse_cansituency,dont_filter=True)
            
    def parse_cansituency(self,response):
        
        consituency_urls = response.xpath('//table[@class="table"]/tbody/tr/td[2]/a/@href').getall()
        
        for consituency_url in consituency_urls:
            absoulte_party_url = urljoin(response.url,consituency_url)
            yield scrapy.Request(absoulte_party_url,callback=self.parse_candidate,dont_filter=True)
            
            
            
            
            
            
            
    def parse_candidate(self,response):
        finalData = {}
        self.count += 1
        
        finalData['ref'] = str(self.count)
        
        finalData['']=response.
        
        candidate = response.xpath('//div[@cand-info]/div/div[1]/text()') 
           