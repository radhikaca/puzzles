<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 00:04:34 2020

@author: rad
"""
=======
''' Lattice Points '''

import math as m

r=25


count=0
>>>>>>> d40c517c0c5331f14bef0cfb8d0c58d857b0a3c9
lp=[(0,r),(r,0),(0,-r),(-r,0)]
 # (0,r),(r,0),(0,-r),(-r,0)
for i in range ( 1, r-1):
    yy = r*r - i*i
    y=int(m.sqrt(yy))
    if(y*y==yy):
        lp.extend([(y,i),(i,y),(-y,i),(i,-y)])


print(lp)



        count+=1
        

print(lp)

