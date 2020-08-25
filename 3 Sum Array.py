# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:50:55 2020
3 Sum of Array
@author: rad
"""

class Solution:
    def threeSum(self, nums):
        out=[]
        s=set()
        unique_nos=[]
        l=len(nums) 
        for i in range (0,l):
            for j in range (i+1,l):
                for k in range (j+1,l):
                    if(nums[i]+nums[j]+nums[k]==0):
                        unique_nos=[nums[i],nums[j],nums[k]]
                        #unique_nos.sort()
                        if unique_nos not in out :
                            out.append(unique_nos)
        return out

inp=  [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(inp))