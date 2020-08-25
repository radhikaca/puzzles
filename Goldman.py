# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:29:15 2020

@author: rad
"""
d=[["mar",-12],["rom",-11],["pip",-11],["mar",-11],["mar",-22]]
#d=[["mar",12],["mar",11],["mar",22]]
m={}
for i in d:
     #print(i)
     if(i[0] in m):
        l=m[i[0]]
        l.append(i[1])
     else:
        
        l=[i[1]]
        m[i[0]]=l

max1=0
for k,v in m.items():
    
    avg1=int(sum(v)/len(v))
    if(avg1>max1):
        max1=avg1

print(max1)