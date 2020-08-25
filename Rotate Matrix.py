# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:59:12 2020

@author: rad
"""

nums1 = [1]
nums2 = [1]

from collections import Counter

c1=Counter(nums1)
out=[]

for i in nums2:
     if(c1[i]>=1):
            out.append(i)
            c1[i]-=1
print(out)