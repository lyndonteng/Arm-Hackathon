# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:35:40 2017

@author: Lyndon Teng
"""

import requests


base_url="http://10.25.1.54:5000"

my_dict="23.40 23.22 23.13 23.10 23.09 23.07 23.04 23.03 23.02 23.02 23.02 23.00 22.99 22.96 22.97 22.97 22.96 22.97 22.96 22.96, 68.33 68.20 62.75 56.55 51.26 46.90 43.48 40.61 38.44 36.91 35.72 34.75 34.02 33.51 33.24 32.96 32.74 32.65 32.50 32.38"
payload = my_dict
response = requests.put(base_url, data=payload)

print(response.text) #TEXT/HTML
print(response.status_code, response.reason) #HTTP