# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:58:53 2020

@author: rad
"""

class Stairs:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        
        for i in range(0,n):
            a,b=b,a+b
        return b

n=input("enter # of stairs")
print("# of way to reach ",Stairs().climbStairs(int(n)))