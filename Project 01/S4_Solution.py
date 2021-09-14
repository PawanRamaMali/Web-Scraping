#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import time
import smtplib


while True:
   
    url = "https://pastebin.com/Mfc9txQV"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup =  BeautifulSoup(r.text, 'lxml')
    
    if str(soup).find("Key") == -1:
        
        time.sleep(500)
        
        continue
    
    else:
        
        create_email = 'Subject: CHECK PASTEBIN - FOUND KEY'
        from_address = 'from address'
        to_address = 'to address'
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        #USE SSL RECOMMENDED
        mail.starttls()
        mail.login("USERNAME", "PW")
        mail.sendmail(from_address, to_address, create_email)
        mail.close()
        print("ALERT")
        
        break
    
    
    
    #https://classroom.github.com/a/5b4Gmpqp