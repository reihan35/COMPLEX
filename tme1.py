#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np

def sac_a_dos(R, T_max):
    U = []
    P = []
    
    for i in range(T_max):
        U.append(int(random.uniform(1,R)))
        P.append(int(random.uniform(1,R)))

    b = int((1/2) * np.sum(np.array(P)))

    return U, P, b

def algo_glout(sac):
    print("instance de sac : " , sac)
    l2 = []
    psac = 0
    sac_fin = []
    
    T_max = len(sac[0])
    U = sac[0]
    P = sac[1]
    b = sac[2]
    
    for i in range(T_max):
        l2.append((U[i]/P[i],i)) 
     


    l2=sorted(l2, reverse=True)

    #l2.sort(key=lambda x: x[0], reverse=True)
    
    for elem in l2 :
        ind = elem[1]
        if psac + P[ind] < b:
           psac = psac + P[ind]
           sac_fin.append(ind)
           
    return sac_fin



            
    
print(algo_glout(sac_a_dos(10, 5)))