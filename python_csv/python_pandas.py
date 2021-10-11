# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:43:12 2021

@author: jason
"""

import pandas as pd
file = pd.read_html("https://en.wikipedia.org/wiki/Comma-separated_values")

print(len(file))

file[1]
type(file[1])

file[1].to_csv(r'webscrape.csv', index = False)
test_read = pd.read_csv('webscrape.csv')
print(test_read)