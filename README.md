# Web Scraping

Web scraping is the process of using bots to extract content and data from a website. Unlike screen scraping, which only copies pixels displayed onscreen, web scraping extracts underlying HTML code and, with it, data stored in a database. The scraper can then replicate entire website content elsewhere.

Web scraping, also known as web data extraction, is formally known as the process of obtaining and structuring data from the web using intelligent
automation.
It can be used to potentially retrieve hundreds, millions, or even billions of data points from the internet’s seemingly endless frontier.

## Ethics of Scraping

* Do not engage in piracy or other unauthorized commercial use regarding the data you extract.
* Read the ToS and robots.txt of the site you are about to scrape.
* Do not spam the website with multiple requests in a short amount of time, as that may hurt them and/or may be classified as a DDOS attack.

> Websites want to be scraped but not overly scraped - Google 

## HTTP Requests 

* On the web, servers and clients usually communicate through HTTP requests.
* HTTP stands for ‘HyperText Transfer Protocol’ and it specifies how requests and responses are to be formatted and transmitted. 
* These requests are how most of your web surfing is happening. 
* When opening a page, the browser sends a request to the server of that page, and the server responds with the relevant resources (HTML, images, etc.).
* The two most popular request types are GET and POST.

### GET

• Obtain data from server
• Can be bookmarked
• Parameters are added directly into the URL
• Not used to send sensitive info (such as 
passwords)

### POST
• Usually used when a state needs to be altered (such as adding items to you shopping cart) or when sending passwords
• Parameters are added in a separate body, thus it is more secure
• Cannot be bookmarked

### Request headers

* Request headers are pieces of information about the request itself - information, such as the encoding and language of the expected response, the length and type of data provided, who is making the request, cookies and so on. 
* These pieces of information, referred to as headers, are intended to make communications on the web easier and more reliable, as the server has a better idea of how to respond.
* Two of the most common header fields are the `User-Agent` (identification string for the software making the request) and cookies (special type of header that has a variety of uses)


### Response 

* The response contains 2 main pieces of information – the status code and the body of the response.
* The status code indicates whether the request was successful and/or any errors. It is represented by a 3-digit number. 
* The body of the response contains the requested information. Usually, it is either an HTML or a JSON file.

The two most frequently encountered status codes are:
▪ 200 OK – The request has succeeded
▪ 404 Not Found – The server can not find the requested resource

Codes in the ranges indicate:

* 2xx – Success 
* 3xx – Redirects
* 4xx – Client errors 
* 5xx – Server errors


### JSON 

* JSON stands for ‘JavaScript Object Notation’ as it was derived from the JavaScript programming language. It is a standard for data exchange on the web.
* The JSON format relies on 3 key concepts: it should be easy for humans to read and write; easy for programs to process and generate, regardless of the programming language; and, finally: written in plain text.
* It achieves that by using conventions familiar to almost all programmers, by building upon 2 structures: dictionaries and lists.

##### Dictionary 

A dictionary is a data structure that contains key-value pairs, surrounded by curly brackets

##### Lists 

A list, on the other hand, is a collection of items. It is contained inside square brackets.


### API 

An API is an Application Programming Interface.
An API specifies how software components should interact. You may think of it as a contract between a client and a server. If the client makes a request in a specific format, the server will always respond in a documented format or initiate a defined action. Web-based APIs usually provide information.
Some APIs are free, most are either paid, or require registration. In the latter case, you are usually given a KEY and ID that must be incorporated into every request to that API.
Examples of APIs:

![image](https://user-images.githubusercontent.com/11299574/132754261-17a6e535-f15a-4a5f-91ec-5b337b9c2a3f.png)


