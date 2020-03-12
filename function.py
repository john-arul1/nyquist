
N0=complex(1.0E2,0)
lam=complex(0.1,0)
beta=complex(3.0E-3,0)
L=complex(1.0E-6,0)
alpha=complex(1.0E-5,0)


def CF(s):
    w=complex(0,0)
    w=100.0/(s+1)/(s/10+1)
    #w=240.0/(s-4)/(s+9)/(s+5)
    #w =N0/(s*L+s*beta/(lam+s)-alpha*K)   # form1
    w =1.0/L*(lam+s)/(s*(s+lam+beta/L))   # form2  (dn/N0)/dr
    return w
