# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:43:54 2020
Binary Search
@author: rad
"""

arr=[2, 3, 4, 5, 7, 11, 18]

n=2


def search(arr,l,r):
    
    mid=l+(r-l)//2

    if(arr[mid]==n):
        return mid
    else:
        if(arr[mid]>n):
            
            r=search(arr,0,mid-1)
        else:
            r=search(arr,mid+1,len(arr)-1)
            
    return r

print(search(arr,0,len(arr)-1))