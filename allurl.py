#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:03:57 2018

@author: Melina
"""
from selenium import webdriver
import time
browser=webdriver.Chrome()
try:
    browser.get("http://www.zxuew.cn/daodejing/")
                
    urls = browser.find_elements_by_tag_name("a")
 
    for url in urls:
        print(url.get_attribute("href"))
    while True:
        #browser.refresh();
        time.sleep(1)
    

    #print(browser.page_source)
    #time.sleep(10)
finally:
    browser.close()