# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:57:56 2020

@author: rad
"""

def twoSum(num,target):
    dic_map={}
    index=[]
    pairs=[]
    for i in range(len(num)):
        diff=target-num[i]
        if(diff in dic_map):
            index.append((dic_map[diff],i))
            pairs.append((diff,num[i]))
        else:
            dic_map[num[i]]=i

    print(index)
    print(pairs)
    
twoSum([2,4, 7, 11, 15,4,5,8,1],8)
            