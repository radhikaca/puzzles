# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:30:21 2020
Fibonaaci with memoize
@author: rad
"""

def fib(n,memo):
    if(memo[n]!=None):
      return memo[n]
    if(n==1 or n==2):
      result=1
    else:
      result=fib(n-1,memo)+fib(n-2,memo)
    memo[n]=result
    return result

memo=[None]*6
print(fib(5,memo)) 

