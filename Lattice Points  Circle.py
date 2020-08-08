''' Lattice Points '''

import math as m

r=25
count=0
lp=[(0,r),(r,0),(0,-r),(-r,0)]
 # (0,r),(r,0),(0,-r),(-r,0)
for i in range ( 1, r-1):
    yy = r*r - i*i
    y=int(m.sqrt(yy))
    if(y*y==yy):
        lp.extend([(y,i),(i,y),(-y,i),(i,-y)])
        count+=1
        

print(lp)
