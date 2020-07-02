# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('E:\Web_Scrapping\chromedriver.exe')





links={}
driver.get('https://alternativedata.org/data_provider/')
for i in range(1,379):
        a = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/section[2]/table/tbody/tr['+str(i)+']/td[1]/a')
        href = a.get_attribute("href")
        links.setdefault(a.text,[]).append(href)
        
        
for keys in links:
    href = links[keys][0]
    driver.get(href)
    try :
        weblink = driver.find_element_by_xpath("//*[@class='orange']").text
    except :
        weblink = ""                                             
    links[keys].append(weblink)
    try:
        description = driver.find_element_by_xpath("//*[@class='big mt-0']").text
    except :
        description = ""
    links[keys].append(description)
    
    
    
    
    
df = pd.DataFrame.from_dict(links, orient='index')

df.to_csv("Alternative_Data.txt", sep='\t' , index = True )