# Amazon Product Average Price Scraping

This repository will demonstrate how we can use the ```scrapy``` python library in order to conduct web scraping to find out the average price of any amazon product. 

The user needs to enter the product name in the console and the the scrapy ```Spider``` will crawl through the HTTP Request Response to extract the prices from the products that are listed.

This process is known as ```Crawling``` in scrapy. 

## Web Scraping

Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser

![Web-Scraping](https://miro.medium.com/max/1200/1*4BnBQE9Bu-EQ-gGz25x8pg.png)

Web Scraping is essential for a lot of applications, be it data analysis or information gathering. 

There are a lot of libraries available in python that can be used for scraping web-pages and gathering information, however ```scrapy``` is extremely powerful and efficient as it allows us to crawl through multiple web-pages in a systematic structure.

## Scrapy

Scrapy is a free and open-source web-crawling framework written in Python. Originally designed for web scraping, it can also be used to extract data using APIs or as a general-purpose web crawler.

### How does it work?

![Scrapy-Working](https://pluralsight.imgix.net/course-images/scrapy-extracting-structured-data-v1.png)

Scrapy is extremely powerful and easy to use. The data from a response can be extracted using ```xpath``` or ```css```. However, I prefer ```css``` because it can be used universally whereas ```xpath``` may not be supported by many browsers

## Program Explanation

As mentioned above, the main idea of the program is based on web-scraping. To create a web-scraping project to scrape data from a particular website, we must first understand how the website HTML is structured. 

1. In this case, we must see how the URL is structured whenever we search for a product in the amazon search-box. We will use this URL to extract data:

![URL-Format](images/search_url.png)

2. After we know the URL which displays the products, we must find out the element used to display the product prices. The product prices are displayed as follows on the amazon website:

![Price-Display](images/listed_prices.png)

3. Now we know how prices are listed on the website. Now we must inspect the HTML to figure out what element is used for this particular price. We will need the tag name and the class name for that element to extract the prices. The HTML tag can be seen as: 

![Inspected-Element](images/inspected_element.png)

4. Our spider crawls through this URL and extracts the prices using the tag and class name specified, displaying the result.

## Result

After all the prices have been fetched, the program displays the mean value of all the prices, giving us the average price for our desired product:

![Average-Price-Result](images/result.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)