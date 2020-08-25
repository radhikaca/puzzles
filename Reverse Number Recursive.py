# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:10:40 2020
Reverse a string recursively
@author: rad
"""
rev=0
def rev_func(q):
    global rev
    if q>0:
        r=q%10
        rev=rev*10+r
        rev_func(q//10)

    return rev

r=rev_func(1236)
print(r)