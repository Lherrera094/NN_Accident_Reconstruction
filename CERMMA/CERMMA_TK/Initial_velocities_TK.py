#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import numpy as np
import math as mp


# %%


#Final result of the initial speed
def initial_speed(U_R,alph,lamb):
    u = []
    
    for i in range(3):
        U = U_R[i]*(np.sin(mp.radians(lamb[i]))/np.sin(mp.radians(alph)))
        u.append(U)
    
    return u


# %%


#Closing speed parallel component
def closing_speed_par(E,m1,m2,d1,d2,e):
    dU_p = []
    
    for ei in e:
        U_p = 2*E*((m1*d2)+(m2*d1))/(m1*m2*(1-ei**2))
        dU_p.append(np.sqrt(U_p))
    
    return dU_p


# %%


#Closing speed perpendicular component
def closing_speed_trans(dV,m1,K1,h1,h1t,m2,K2,h2,h2t):
    dU_t = []
    
    for v in dV:
        f = ((h1t*h1)/(m1*K1**2)) + ((h2t*h2)/(m2*K2**2))
        dU_t.append(m1*v*f)
    
    return dU_t


# %%


#Obtains beta and resultant closing speed
def beta_and_resU(dU_p,dU_t):
    U_R, beta = [], []
    
    for i in range(3):
        U_R.append( np.sqrt( dU_p[i]**2 + dU_t[i]**2 ) )
        tan_b = dU_t[i]/dU_p[i]
        beta.append( np.degrees(np.arctan(tan_b)) )
    
    return U_R, beta


# %%




