#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#imports

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#options = webdriver.ChromeOptions()
#options.add_argument('--incognito')


driver = webdriver.Chrome()
driver.get('http://sdsclub.com')
time.sleep(5)

#links
button_one = driver.find_element_by_xpath('//*[@id="menu-item-456"]/a').click()
time.sleep(5)

button_two = driver.find_element_by_xpath('//*[@id="category-career"]/div/div[2]/div[4]/div/a/img').click()
time.sleep(10)

button_close = driver.find_element_by_class_name('close-icon').click()

time.sleep(5)

#add parser
page_source = driver.page_source
soup =  BeautifulSoup(page_source, 'lxml')

#add scrape info
scrape_one = [i.text for i in soup.findAll('span', {'class': 'desc'})]
scrape_two = [i.text for i in soup.findAll('div', {'class': 'single-path-article-content'})]
scrape_three = [i.text for i in soup.findAll('p', {'class': 'name'})]

#assign DF's
df = pd.DataFrame(scrape_one)
df_two = pd.DataFrame(scrape_two)
df_three = pd.DataFrame(scrape_three)

#print data
print(df, df_two, df_three)

time.sleep(10)

driver.quit()


df_scrape_one_clean = df.replace('\n', ' ', )
df_scrape_two_clean = df_two.replace('\n', ' ', )
df_scrape_three_clean = df_three.replace('\n', ' ',)
clean_stack = pd.concat([df_scrape_one_clean, df_scrape_two_clean, df_scrape_three_clean], axis=1)


#https://clasroom.github.com/a/WYb3hT_P


