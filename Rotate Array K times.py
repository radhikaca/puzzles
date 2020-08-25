# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:10:14 2020

@author: rad
"""

def reverse(nums,start,end):
        # speed up the rotation
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1


nums=[1,2,3,4,5]
k=4

k%=len(nums)
reverse(nums, 0, len(nums)-1)
reverse(nums,0,k-1)
reverse(nums,k,len(nums)-1)
print(nums)