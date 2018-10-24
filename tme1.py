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

    b = int(1.0/2 * np.sum(np.array(P)))

    return U, P, b

def algo_glout(sac):
    #print("instance de sac : " , sac)
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
           sac_fin.append((ind,1))
           
    u_sac_fin = 0
    
    for (i_obj, r_obj) in sac_fin:
        u_sac_fin += U[i_obj] * r_obj
        
    return u_sac_fin

def algo_glout_frac(sac):
    #print("instance de sac : " , sac)
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
        if psac + P[ind] <= b:
           psac = psac + P[ind]
           sac_fin.append((ind,1))
        else:
           r = ((b - psac) * 1.0) / P[ind]
           psac = psac + P[ind] * r
           sac_fin.append((ind, r))
        
    u_sac_fin = 0
    
    for (i_obj, r_obj) in sac_fin:
        u_sac_fin += U[i_obj] * r_obj
        
    return u_sac_fin


def b_and_b_1(sac):
    U = np.array(sac[0])
    P = np.array(sac[1])
    b = np.array(sac[2])
    n = len(U)
    
    pile = []
    binary_list = np.zeros(n)
    
    solutions = []
    pile = [(binary_list, 0)]
    print(sac)
    
    best_s= []
    best_v = 0 
    b_sup = algo_glout_frac(sac)
    b_inf = algo_glout(sac)
    
    print("b_sup, b_inf", b_sup, b_inf)
    
    while pile != []:
        current_blist, i = pile.pop()
        
        if i == 0:
            ind = np.argwhere(current_blist == 1)
            u_ind = U[ind]
            p_ind = P[ind]
            
            marwan = np.argwhere(current_blist == 0)
            b_sup = algo_glout_frac((U[marwan],P[marwan],b-p_ind.sum())) + u_ind.sum()
            new_b_inf = algo_glout((U[marwan],P[marwan],b-p_ind.sum())) + u_ind.sum()
            b_inf = min(new_b_inf, b_inf)
            
            print(b_inf, b_sup)
            if b_sup < b_inf:
                continue
        
        
        if i != n:
            new_blist = current_blist.copy()
            new_blist[i] = 1
            
            pile.append((new_blist, i+1))
            pile.append((current_blist, i+1))
        else:
            s_u = np.array(U[np.argwhere(current_blist == 1.)]).sum()
            s_p = np.array(P[np.argwhere(current_blist == 1.)]).sum()
            
            if s_p > b:
                continue
            if best_v < s_u:
                best_s = current_blist
                best_v = s_u
                
            solutions.append(current_blist)
          
    return np.argwhere(best_s == 1)
            

#sac = sac_a_dos(10,2)
#print(sac)
#print(algo_glout_frac(([4, 2], [7, 5], 6)))
print(b_and_b_1(sac_a_dos(30,5)))    
