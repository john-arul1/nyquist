# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 08:48:57 2020

@author: john
"""

#import control
import matplotlib.pyplot as plt
from scipy import signal

"""
scipy
The following gives the number of elements in the tuple and the interpretation:

            1 (instance of lti)

            2 (num, den)

            3 (zeros, poles, gain)

            4 (A, B, C, D)

"""
num = [2]
den = [1,-1]
#5/(s+1)
s1 = signal.TransferFunction(num,den)
#s1 = signal.ZerosPolesGain([], [1, 1, 1], [5])
w,H=signal.freqresp(s1)

#Creating a transfer function G = num/den
#G = control.tf(num,den) 
#control.nyquist(G)
#fig,ax=plt.subplots()
#plt.figure()
plt.plot(H.real, H.imag, "b")
plt.plot(H.real, -H.imag, "r")

x=H.real
y=H.imag
ci=int(len(x)/2)
dx=x[ci+1]-x[ci]
dy=x[ci+1]-y[ci]

#plt.arrow(x,y,dx,dy,shape='full', lw=1, length_includes_head=True, head_width=5.0)

#plt.quiver(x[ci],y[ci],dx,dy,headwidth=0.2)

plt.title('Nyquist Diagram of G(s)H(s) = 5/(s+1)(s+2)(s+3)')
plt.xlabel('Real axis',fontsize=14)
plt.ylabel('Imaginary axis',fontsize=14)
plt.grid(True)
plt.show()


