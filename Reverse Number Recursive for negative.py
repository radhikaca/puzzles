# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:53:01 2020

@author: rad
"""

class Solution:
    s=0
    
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        
        while (x>0):
            r=x%10
            Solution.s=Solution.s*10+r
            x=x//10
        
        return Solution.s*sign

t=Solution()
print(t.reverse(-123))

