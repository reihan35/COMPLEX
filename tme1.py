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

def b_and_b_1(sac):
    U = np.array(sac[0])
    P = np.array(sac[1])
    b = np.array(sac[2])
    n = len(U)
    
    pile = []
    
    #current_solution = []
    #current_p = []
    #pile.append(current_solution)
    
    binary_list = np.zeros(n)
    
    solutions = []
    pile = [(binary_list, 0)]
    
    while pile != []:
      #  print(pile)
        current_blist, i = pile.pop()
        #print(i)
        if i != n:
            new_blist = current_blist.copy()
            new_blist[i] = 1
            
            pile.append((new_blist, i+1))
            pile.append((current_blist, i+1))
        else:
             #print(pile)
            solutions.append(current_blist)
            
    best_u = 0
    best_s = []


    s_u = 0
        smax = 0
        pmax = 0
        somme = 0
        poids = 0
    #print(solutions)
    for s in solutions:
        s = np.array(s)
        #print(s, np.array(U[np.argwhere(s == 1.)]),np.array(P[np.where(s == 1.)]))
        #s_u = np.array(U[np.argwhere(s == 1.)]).sum()
        #s_p = np.array(P[np.argwhere(s == 1.)]).sum()
        
            for i in x :
                somme = somme + U[i]
                poids = poids + P[i]
            if somme > smax:
                smax = somme 
        
        print(s, s_u, s_p)
        if s_p > b:
            continue
        else:
            if best_u < s_u:
                best_u = s_u
                best_s = s
                
    return best_s
            
sac = sac_a_dos(10,2)
print(sac)
print(b_and_b_1(sac_a_dos(10,2)))    
#print(sac_a_dos(10,2))
#print(algo_glout(sac_a_dos(10, 5)))