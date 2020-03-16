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


xy_plot=0
uv_plot=1

NTP=5000  # N Total number of points
nop=1000    # Number of points per detour arc

r=0.001     # detur arc radius
R=100     #  maxiumum w of -jw, jw

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
fig=plt.figure

if xy_plot==1:
    #fig,(ax1,ax2)=plt.subplots(1,2,sharey=False)
    #ax1.plot(rx, ry,color='blue')
    plt.plot(lxx, lyy,color='blue')
    plt.plot(Rx,Ry,color='red')
    
    # plot arrow to be done
    ci=int(len(Rx)/3)
    dx=(Rx[ci+2]-Rx[ci])
    dy=(Ry[ci+2]-Ry[ci])
    plt.arrow(Rx[ci],Ry[ci],dx,dy,shape='full', lw=1, length_includes_head=True, head_width=5.0)
    #plt.quiver(Rx[ci],Ry[ci],dx,dy, units='xy', scale=0.1,
    #          scale_units='xy', color='red')
# complex mapping
#sp1=[complex(px,py)  for px,py in zip(rx,ry)]
sp1=[complex(px,py)  for px,py in zip(lxx,lyy)]
u,v=cmap(sp1)
sp2=[complex(px,py)  for px,py in zip(Rx,Ry)]
Ru,Rv=cmap(sp2)

#plot arrow to be done
if uv_plot==1:
 
    #plot u,v plane
    plt.plot(u[:],v[:],color='blue')
    plt.plot(Ru,Rv, 'red')
    plt.text(-2.5,-0.0,r'$\alpha=1.0E-4$',fontsize=14)
    #ci=2550#
    ci=3513
    dx=u[ci+1]-u[ci]
    dy=v[ci+1]-v[ci]
    plt.arrow(u[ci],v[ci],dx,dy,shape='full', lw=0.1, length_includes_head=False, head_width=0.15)
   
    
margin_plot=0    
if margin_plot==1:    
    th=np.linspace(0,-2*Pi,100)  # 0, -pi/2, -pi,-2pi
    Rc=[cmath.rect(1.0,t) for t in th]
    rx=[s.real for s in Rc]
    ry=[s.imag for s in Rc]
    plt.plot(rx,ry,'-.')
    s=[complex(x,y) for x,y in zip(u[3500:],v[3500:])]
    u1=10.0
    u2=10.0
    v1=10.0
    v2=10.0
    Pm=0.0
    Gm=0.0
    import time
    for s1 in s:
#        print (cmath.phase(s1))
#        time.sleep(1)
        if abs(abs(cmath.phase(s1))-Pi) < 0.04: #  and (abs(s1) > 0.2):
           Gm=1.0/abs(s1)
           #Gm=20.0*np.log10(Gm) 
           u2=s1.real
           v2=s1.imag
        #print (cmath.phase(s1)*180/Pi)   
        if abs(abs(s1)-1.0) < 0.05 : # and (abs(cmath.phase(s1)) -Pi) < 1.0E-4:
           Pm = (cmath.phase(s1)+Pi)*180.0/Pi
           u1=s1.real
           v1=s1.imag
    
    print (Gm,Pm)       
    x1=[0,u1]
    y1=[0,v1]   
    plt.plot(x1,y1,'red')
    x2=[0,u2]
    y2=[0,v2]
    plt.plot(x2,y2,'red')
    #plot Gain and Phase Margins
    plt.text(-0.5,0.3,r'$\frac{1}{|GH(\omega_{cp})|}$',fontsize=14)
    th=np.linspace(-Pi,-Pi+17.7/180.0*Pi,10)  # 0, -pi/2, -pi,-2pi
    pharc=[cmath.rect(0.750,t) for t in th]
    rx=[s.real for s in pharc]
    ry=[s.imag for s in pharc]
    plt.plot(rx,ry,'-.',color='grey')
    plt.text(-0.75,-0.4,r'$\phi_m$',fontsize=14)


plt.plot(-1,0,'o',color='green')
#plt.xlim([-2,1])
#plt.ylim([-1,1])
#plt.title('Nyquist Diagram of G(s)H(s) = 240/((s-4)(s+9)(s+5))')
#tf=r'$\frac{K}{(s(s+1.0)^2 )}$'
tf=r'$\frac{-\alpha*N0/\Lambda*(s+\lambda)}{(s*(s+\lambda+\beta/\Lambda))}$'
plt.title('Nyquist Diagram of G(s)H(s) ='+tf,fontsize=16)
plt.xlabel('Real axis',fontsize=14)
plt.ylabel('Imaginary axis',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)



plt.grid()
plt.savefig('ex1.jpg',bbox_inches='tight')

#plt.show()


#savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#        orientation='portrait', papertype=None, format=None,
#        transparent=False, bbox_inches=None, pad_inches=0.1,
#        frameon=None, metadata=None)


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



