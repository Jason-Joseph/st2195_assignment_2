# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 22:25:38 2021

@author: Christopher Redian
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Comma-separated_values"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

table = soup.find("table" , class_ = "wikitable")


headers = []

for i in table.find_all("th"):
    title = i.text.strip()
    headers.append(title)
    

df = pd.DataFrame(columns = headers)

for row in table.find_all("tr")[1:]:
    data = row.find_all("td")
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data 
    
    df.to_csv(r'webscrape.csv', index = False)

    test_read = pd.read_csv('webscrape.csv')
    print(test_read)
    


    
