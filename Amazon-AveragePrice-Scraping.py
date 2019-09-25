#Importing all the necessary libraries we need
import scrapy
import numpy as np
from scrapy.crawler import CrawlerProcess

#Initializing some global variables
search_val = ""
amazon_link = "https://www.amazon.in/s?k=SEARCHVALUE&ref=nb_sb_noss_2"
spider_stats = {}
result_prices = []

#Creating our Spidey class to scrawl through the request
class AmazonSpider(scrapy.Spider):
    name = "Amazon-Spider"

    #Specifying the URL and sending a Request
    def start_requests(self):
        global search_val
        global amazon_link

        #Replacing the default search value with the keyword we enter for search
        search_link  = amazon_link.replace("SEARCHVALUE",search_val.replace(' ','+'))
        yield scrapy.Request(url=search_link, callback=self.get_values)

    #Parse function used to get the required value from the response(GET)
    def get_values(self, response):
        global result_prices
        global spider_stats

        #Grabbing the values using the css function from the webpage response
        values = response.css('span.a-price-whole ::text')
        result_prices = values.extract()

        #Extracing the stats about the entire process
        spider_stats = self.crawler.stats.get_stats()


if __name__ == "__main__":

    #Allowing user to enter the price of the product they want to search the prices for
    search_val = input("Enter the item you want to search:")

    #Creating a crawler process
    process = CrawlerProcess({ 'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    process.crawl(AmazonSpider)
    process.start()

    #Converting prices from string to float-type list
    prices = [float(price.replace(',','')) for price in result_prices if price != '.']

    #Printing out the average value from all the prices
    print(f"The average price for {search_val} is :{np.mean(prices)} rupees! (Elapsed in {spider_stats['elapsed_time_seconds']} seconds!)")
