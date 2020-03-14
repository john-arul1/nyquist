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
from function import * 
import cauchy

#constants
Pi=np.pi


NTP=10000  # N Total number of points
nop=100    # Number of points per detour arc

r=0.01     # detur arc radius
R=100     #  maxiumum w of -jw, jw
Rinf=int(1.0E3)

shift=0.0

# imaginary part of poles on jy axis 
#arcs=[]
#arcs=[]  # defined in  function file

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
    NOP=int(NTP/(narc+1))
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
        print ("error in detour specification-over lap between arcs")
        print ()
        exit(1)


#generate detours
th=np.linspace(-Pi/2.0,Pi/2.0,nop)
Rc=[cmath.rect(r,t) for t in th]
rx=[s.real for s in Rc]
ry=[s.imag for s in Rc]

lst_arcs=[]   # arc coordinates  ry are shifted
for i in range(narc):
    ryp=[ry1+arcs[i] for ry1 in ry]
    lst_arcs+=[ryp]
    
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
        ly= np.append(ly,lst_arcs[j])
        lx= np.append(lx, rx)
    

lxx=lx
lyy=ly
Rinf=R

th=np.linspace(Pi/2.0,-Pi/2.0,NTP)
Rc=[cmath.rect(Rinf,t) for t in th]
Rx=[s.real for s in Rc]
Ry=[s.imag for s in Rc]

#union of s plane segments lines , detours and sni-circle

fig,(ax1,ax2)=plt.subplots(1,2,sharey=False)
#ax1.plot(rx, ry,color='blue')
ax1.plot(lxx, lyy,color='blue')
ax1.plot(Rx,Ry,color='red')

# plot arrow to be done
#ci=int(len(Rx)/2)
#dx=(Rx[ci+2]-Rx[ci])
#dy=(Ry[ci+2]-Ry[ci])
#ax1.arrow(Rx[ci],Ry[ci],dx,dy,shape='full', lw=1, length_includes_head=True, head_width=2.0)

# complex mapping
#sp1=[complex(px,py)  for px,py in zip(rx,ry)]
sp1=[complex(px,py)  for px,py in zip(lxx,lyy)]
u,v=cmap(sp1)
sp2=[complex(px,py)  for px,py in zip(Rx,Ry)]
Ru,Rv=cmap(sp2)

ax2.plot(u,v,color='blue')
ax2.plot(Ru,Rv, 'red')


#plot arrow to be done
#ci=int(len(u)/2)
#dx=u[ci+2]-u[ci]
#dy=v[ci+2]-v[ci]
#
#ax2.arrow(u[ci],v[ci],dx,dy,shape='full', lw=0.5, length_includes_head=True, head_width=0.2)

#ax2.plot(-1,0,'o',color='green')
plt.xlim([-2,2])
plt.ylim([-1,1])
plt.grid()
plt.show()

# Cauchy plot
flg_cauchy=0
if flg_cauchy ==1:
    x,y,u,v = cauchy.Cauchy(1000,20)
    fig,(ax1,ax2)=plt.subplots(1,2,sharey=False)
    ax1.plot(x,y,color='blue')
    
    ci=int(len(x)/2)
    dx=x[ci+2]-x[ci]
    dy=y[ci+2]-y[ci]
    ax1.arrow(x[ci],y[ci],dx,dy,shape='full', lw=1, length_includes_head=True, head_width=1)

    ax2.plot(u,v,color='red')
    dx=u[ci+2]-u[ci]
    dy=v[ci+2]-v[ci]
    
    ax2.arrow(u[ci],v[ci],dx,dy,shape='full', lw=1, length_includes_head=True, head_width=0.01)
    
    plt.grid()
    plt.show()



