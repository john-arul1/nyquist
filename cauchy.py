# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:49:13 2020

@author: john
"""
import numpy as np
import cmath
from function import * 

Pi=np.pi

def Cauchy (NP,r):
    th=np.linspace(0,-2*Pi,NP)  # 0, -pi/2, -pi,-2pi
    Rc=[cmath.rect(r,t) for t in th]
    rx=[s.real for s in Rc]
    ry=[s.imag for s in Rc]
    sp=[complex(px,py)  for px,py in zip(rx,ry)]
    u,v=cmap(sp)
    return rx,ry,u,v


#fig,(ax1,ax2)=plt.subplots(1,2,sharey=False)
#ax1.plot(rx, ry,color='blue')
#ax2.plot(u, v,color='blue')
#plt.grid()
#plt.show()










