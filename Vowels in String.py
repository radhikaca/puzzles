# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:31:10 2020
Remove vowels from a string
@author: rad
"""

string=input()

d=["a","e","i","o","u"]
str_list=list(string)
for i in d:
    if(str_list.count(i)>0):
        str_list[str_list.index(i)]=''
    
print(''.join(str_list))
