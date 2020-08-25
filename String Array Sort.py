# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:56:23 2020
sort a string array 

@author: rad
"""
import collections as c
str_array=["hello","testing","sorting","of","arrays"]
d={}
for i in str_array:
    d[i]=len(i)

x=c.OrderedDict(sorted(d.items,key=lambda y:y[1],reverse=True))
new_list=[i for i in x.keys()]
print(new_list)
