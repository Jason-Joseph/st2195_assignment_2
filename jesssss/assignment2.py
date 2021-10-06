#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:03:00 2021

@author: jesslynhillary1
"""

import pandas as pd
file = pd.read_html("https://en.wikipedia.org/wiki/Comma-separated_values")
print(len(file))
file[1]
type(file[1])
file[1].to_csv(r'cars', index = False)
cars_csv = pd.read_csv('cars')
print(cars_csv)