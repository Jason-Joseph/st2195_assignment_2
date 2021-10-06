#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:59:51 2021

@author: MIchelle
"""

import pandas as pd
file = pd.read_html("https://en.wikipedia.org/wiki/Comma-separated_values")
print(len(file))
file[1]
type(file[1])
file[1].to_csv(r"webscrap.csv", index = False)
test_read = pd.read_csv(r'webscrap.csv')
print(test_read)