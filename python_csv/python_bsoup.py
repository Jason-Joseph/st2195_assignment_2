# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:52:14 2021

@author: jason
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Comma-separated_values'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

cars_table = soup.find('table', class_ ='wikitable')

headers = []

for i in cars_table.find_all('th'):
    title = i.text
    headers.append(title)
    
df = pd.DataFrame(columns = headers)

for row in cars_table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text for td in data]
    length = len(df)
    df.loc[length] = row_data
    
df.to_csv(r'C:\UOL\Programming for Data Science\Block 2 Lecture Slides\Practice Assignments\Python_csv\bsoup.csv', index = False)

testread = pd.read_csv('bsoup.csv')
print(testread)
  
    