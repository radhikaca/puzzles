# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:19:12 2020
2 sum
@author: rad
"""
prevMap={}
class Solution:
    
        def threeSum(self,nums,target):
            #prevMap={}
            l=[]
            for i in range(0,len(nums)-1):
                diff=target-nums[i]
                indx=i+1
                sub_list=self.twoSum(nums[indx:],diff)
                print(nums[i],diff,nums[indx:],sub_list)
                if(len(sub_list)>0):
                    l.append([nums[i]]+sub_list)
                    print(l)
                else:
                    continue
            return l
            
        def twoSum(self,nums, target):
            
            global prevMap  # val : index
            #print(prevMap)
            for i, n in enumerate(nums):
                diff = target - n
                if diff in prevMap:
                    print(prevMap)
                    return [diff,n]
                prevMap[n] = i
                print(prevMap)
    
            return []

print(Solution().threeSum([-1, 0, 1, 2, -1, -4],0))