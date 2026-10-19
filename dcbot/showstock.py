# -*- encoding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()    #new version selenium is no need t set path
driver.get('https://www.wantgoo.com/stock/ranking/volume')  
time.sleep(2)
names = driver.find_elements(By.CLASS_NAME, 'zw')    
prices = driver.find_elements(By.CSS_SELECTOR, 'td[c-model-dazzle^="class:upDn,text:close"]') 

for i in range(50):
    print(names[i].text,prices[i].text)


driver.quit()
