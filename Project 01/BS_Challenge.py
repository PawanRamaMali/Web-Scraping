#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def review_count_scrape():
    url = 'https://www.amazon.com/Best-Sellers/zgbs'
    headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    print(r.status_code)
    product_total_review = [i.text for i in soup.findAll('a', {'class': 'a-size-small a-link-normal'})]
    df = pd.DataFrame(product_total_review)
    print(df)
    
    #add timer
    time.sleep(60)
    

end_timer = time.time() + 60 * 2
while time.time() < end_timer:
    review_count_scrape()