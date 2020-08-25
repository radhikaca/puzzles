# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:37:48 2020

@author: rad
"""

import requests

url='https://api.github.com/search/repositories?q=language:python&sort=stars'

r=requests.get(url)

response=r.json()
response_count=response['total_count']
response_items=response['items'][1]

print(response_items['tags_url'])