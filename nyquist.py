# -*- coding: utf-8 -*-
"""

Program to plot  Nyquist plot 

written by John Arul


10, March 2020


"""

import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy.geometry import * 
Pi=math.pi
import function #import * 

# parameters of function

#K=complex(1.0E2,0)
#lam=complex(0.1,0)
#beta=complex(3.0E-3,0)
#L=complex(1.0E-6,0)




def cmap(sp):   
    #takes an array and computes the function defined in function.py
    u=[]
    v=[]
    for s in sp:
        w=function.CF(s)
        u.append(w.real)
        v.append(w.imag)

    u=np.array(u)
    v=np.array(v)
    return u,v




#constants
NTP=5000  # N Total number of points
nop=50    # Number of points per detour arc
r=1.0     # detur arc radius
R=500     #  maxiumum w of -jw, jw


arcs=[0]  # imaginary part of poles on jy axis
narc=len(arcs)


lx=[]
ly=[]
Rx=[]
Ry=[]

#generate points along imaginary axis
if narc > 0:
    NOP=int(NTP/narc)
else:
    NOP=NTP    

#generate detours
th=np.linspace(-Pi/2.0,Pi/2.0,nop)
Rc=[cmath.rect(r,t) for t in th]
rx=[s.real for s in Rc]
ry=[s.imag for s in Rc]

lst_circy=[]   # arc coordinates  ry are shifted
for i in range(narc):
    ryp=[ry1+arcs[i] for ry1 in ry]
    lst_circy+=[ryp]
    
NSEG=narc+1    

#build segment array 
# alternate segment and arc    [-R,r1,r2,r3,r4,R]   ndet =2
yseg=[-R]
for i in range(narc):
    yseg+=[arcs[i]-r,arcs[i]+r]
    
yseg+=[R]
    
    
for i in range(NSEG+1): 
    
    if i % 2 == 0:
        lys=np.linspace(yseg[i],yseg[i+1],NOP)      
        lxs=np.zeros(len(lys))
        ly=np.append(ly,lys)
        lx=np.append(lx,lxs)
    else:
        #detour arc
        ly= np.append(ly,lst_circy[i-1])
        lx= np.append(lx, rx)
    



th=np.linspace(Pi/2.0,-Pi/2.0,NTP)
Rc=[cmath.rect(R,t) for t in th]
Rx=[s.real for s in Rc]
Ry=[s.imag for s in Rc]


#union of s plane segments lines , detours and sni-circle

fig,(ax1,ax2)=plt.subplots(1,2,sharey=False)
ax1.plot(lx, ly,color='blue')
ax1.plot(Rx,Ry,color='red')


# complex mapping
sp=[complex(px,py)  for px,py in zip(lx,ly)]
u,v=cmap(sp)
sp=[complex(px,py)  for px,py in zip(Rx,Ry)]
Ru,Rv=cmap(sp)

ax2.plot(u,v,color='blue')
ax2.plot(Ru,Rv, 'red')


plt.grid()
plt.show()

