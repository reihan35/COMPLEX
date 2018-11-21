#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:03:16 2018

@author: 3522144
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def divis_pos(n):
    l=[]
    for x in range(1,n+1):
        if n%x == 0:
            l.append(x)

    return l

def my_gcd(a,b):
    la=divis_pos(a)
    lb=divis_pos(b)

    lc=[]
    if a == 1:
        return b
    if b == 1:
        return a
    
    for x in la:
        for y in lb:
            if x==y:
                lc.append(x)

    return max(lc)

def algo_euclide(a,b) :
    if (b==0) :
        return(a)
    else :
        r=a%b
        return algo_euclide(b,r)


def table(n):
    l=[]
    for x in range(0,n):
        tmp=[]
        for y in range(0,n):
            tmp.append(x*y%n)
        l.append(tmp)

    return l

def my_inverse(n,a):
    lt=[]
    l=table(n)
    
    for x in l[a]:
        if x==1:
            return l[a].index(x)
    return -1


"""t_m = 0
start_time = time.time()
t_m = t_m + (time.time() - start_time)"""

T_pgcd = []
T_inverse = []
a = 5
# b = 

"""for n in range(10, 10000, 10):
    start_time = time.time()
    my_inverse(n,a)
    T_inverse.append(time.time() - start_time)
    
plt.plot(np.arange(10,10000, 10), T_inverse)
plt.show()
"""
print(algo_euclide(10000,86))

a = 100000000000000000000000000000000000000000000000000000
print(a)
start = 1000000000000000
for b in range(start,a,100000000000000000000000000000):
#for b in [10**5, 10**10, 10**15, 10**20, 10**25]:
    start_time = time.time()
    algo_euclide(a,b)
    T_pgcd.append(time.time() - start_time)
    
x = np.arange(start, a, 100000000000000000000000000000)
plt.plot(x, T_pgcd)
plt.show()
#k = np.argmax(T_pgcd)
#print(x[k], T_pgcd[k])

#print(table(5))x
#print(my_inverse(11,3))