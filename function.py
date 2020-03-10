
K=complex(1.0E2,0)
lam=complex(0.1,0)
beta=complex(3.0E-3,0)
L=complex(1.0E-6,0)
alpha=complex(1.0E-5,0)


def CF(s):
    w=complex(0,0)
    #w=240.0/(s-4)/(s+9)/(s+5)
    w =K/(s*L+s*beta/(lam+s)-alpha*K)
    return w
