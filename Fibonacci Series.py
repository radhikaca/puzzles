# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:58:07 2020
Recursive Fibonacci
@author: rad
"""

def fib(n):
    if(n==0 or n==1):
        return 1
    return fib(n-1)+fib(n-2)

n=int(input())
print(fib(n-2))