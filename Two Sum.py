# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:03:34 2020
2 Sum
@author: rad
"""
final=[]
from typing import List
class Solution:
    global final
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap=set()
        
        
        for n in nums:
            diff=target-n
            if(diff in hashMap):
                final.append((diff,n))
                
            hashMap.add(n)
        
Solution().twoSum([2, 7, 11, 15,4,5,3,3],6)
print(final)