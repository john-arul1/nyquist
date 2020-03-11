# -*- coding: utf-8 -*-
"""

Program to plot  Nyquist plot 

written by John Arul


10, March 2020


"""

import cmath
import numpy as np
import matplotlib.pyplot as plt
from sympy.geometry import * 
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
Pi=np.pi

NTP=5000  # N Total number of points
nop=50    # Number of points per detour arc
r=1.0     # detur arc radius
R=50     #  maxiumum w of -jw, jw


# imaginary part of poles on jy axis 
arcs=[]

f1=open('axis_poles.txt','r')
txt=f1.readline()
arctxt=txt.split(',')
arcs=[float(val) for val in arctxt]
f1.close()

arcs=[]

narc=len(arcs)


# check if poles are closer than the detour arcs
if  narc >= 2:
    arcs.sort()
    dif=[y-x for x,y in zip(arcs[:-1],arcs[1:]) ]
    if r >= min(dif)/2.0:
       r= min(dif)/2.2 
  

lx=[]
ly=[]
Rx=[]
Ry=[]

#generate points along imaginary axis
if narc > 0:
    NOP=int(NTP/narc)
else:
    NOP=NTP    


# alternate segment and arc    [-R,r1,r2,r3,r4,R]   ndet =2
yseg=[-R]
for i in range(narc):
    yseg+=[arcs[i]-r,arcs[i]+r]
   
yseg+=[R]

# check for consistency
for i in range(len(yseg)-1):
    if yseg[i+1] < yseg[i]:
        print ("error in dettour specification-over lap between arcs")
        print ()
        exit(1)


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
    
for i in range(NSEG+narc): 
    
    if i % 2 == 0:
        lys=np.linspace(yseg[i],yseg[i+1],NOP)      
        lxs=np.zeros(len(lys))
        ly=np.append(ly,lys)
        lx=np.append(lx,lxs)
    else:
        #detour arc
        j=int((i-1)/2)
        ly= np.append(ly,lst_circy[j])
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


# min max v in uv plane
minv=min(Rv)
miny=min(v)
maxv=max(Rv)
maxy=max(v)
a=min(minv,miny)
b=max(maxv,maxy)

# not used

ax2.plot(-1,0,'o',color='green')
#plt.xlim([-5 ,5])
#plt.ylim([-1,1])
plt.grid()
plt.show()

