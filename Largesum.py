# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:36:42 2020

@author: rad
"""
def fibonacci():
    """Fibonacci numbers generator, first n"""
    a, b, i = 0, 1, 0
    
    while i<10:
        yield i
        #yield a
        #a, b = b, a + b
        i += 1
f = fibonacci()

for i in f:
    print(i)
