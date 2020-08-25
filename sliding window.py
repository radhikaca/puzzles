# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:40:31 2020
Sliding Window
@author: rad
"""

l=[1,3,-1,-3,5,3,6,7]
k=2
op=[]
for i in range(len(l)-k+1):
    op.append(max(l[i:i+k]))
print(op)