
import numpy as np

N0=complex(1.0E0,0)
lam=complex(0.1,0)
beta=complex(3.0E-3,0)
L=complex(1.0E-6,0)
alpha=complex(1.0E-4,0)
#alpha=complex(0.0,0.0)


# poles on imag axis
arcs=[0]

def CF(s):
    K1=1.1
    K2=1.0
    #w=K1/(s-1)
    #w=K1/(s*(s+1.0)**2)
    #w=K1/(s*(s-1.0))
    #w=(1+K2*s)/(s*(s-1.0))
    #w=240.0/((s-4.0)*(s+9.0)*(s+5.0))
            
    #w=240.0/(s-4)/(s+9)/(s+5)
    #w =N0/(s*L+s*beta/(lam+s)-alpha*N0)   # form1
    w =-alpha*N0/L*(lam+s)/(s*(s+lam+beta/L))   # form2  (dn/N0)/dr
    return w


def cmap(sp):   
    #takes an array and computes the function defined in function.py
    u=[]
    v=[]
    for s in sp:
        w=CF(s)
        u.append(w.real)
        v.append(w.imag)
    
    u=np.array(u)
    v=np.array(v)
    return u,v
