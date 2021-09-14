#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from selenium import webdriver

driver = webdriver.Chrome()
#time.sleep(5)

def site_login():
    driver.get('https://www.superdatascience.com/login')
    driver.find_element_by_name('email').send_keys("THISISMYEMAILHERE")
    driver.find_element_by_name('password').send_keys("12345678910")
    driver.find_element_by_xpath('//*[@id="__blaze-root"]/div/div[1]/div/div/form/button').click()
    


site_login()
time.sleep(20)

driver.quit()


    
