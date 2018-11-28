#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:03:16 2018

@author: 3522144
"""
from math import *

'''

import numpy as np
import matplotlib.pyplot as plt
import time
import random
from math import *

def divis_pos(n):
    l=[]
    for x in range(1,n+1):
        if n%x == 0:
            l.append(x)

    return l
'''

'''
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



def my_inverse(a, n):
    t = 0
    newt = 1
    r = n
    newr = a
    
    while newr != 0:
        quotient = r / newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)
    print(r)
        
    if r > 1:
        return -1
    if t < 0:
        t = t + n
    return t

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
'''
def my_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

def my_gcd(a,b) :
    if (b==0) :
        return(a)
    else :
        r=a%b
        return algo_euclide(b,r)

def l(n):
    if log(n)/log(2) - int(log(n)/log(2)) == 0 : 
		return [int(log(n)/log(2))]
    else: 
		#print(log(n)/log(2))
        return [int(log(n)/log(2))] + l(n-(2**int(log(n)/log(2))))

def binary(n,z):
	l = []
	#print(z)
	for i in range (0,int(log(n)/log(2))+1):
		#print(i)
		if i in z :
			l.append(1)
		else:
			l.append(0)
	return l[::-1]

#print(binary(4,l(4))) 


def exp_dis_bin(N,g,n):
	h=1
	print(n)
	for i in range (len(n)-1,0-1,-1):
		#print(i)
		h = (h**2)%N
		print("ici " + str(h))
		if n[i]==1:
			h=(h*g)%N
			#print(h)
	return h

def modular_pow(base, exponent, modulus):
	result=1
	while (exponent > 0):
		base = (base * base)%modulus
		if ((exponent%2) == 1):
			result = (result * base)%modulus
		exponent = exponent - 1
	return result

#print(modular_pow(589,73,896))
print(exp_dis_bin(589,73,binary(896,l(896))))
#print(exp_dis_bin(896,589,binary(73,l(73))))

#g^n mod N

"""     
T_pgcd = []
T_inverse = []

i = 10
x = []

while i < 100000000000000000000000000000000000000000000000000000:
#for b in [10**5, 10**10, 10**15, 10**20, 10**25]:
    x.append(i)
    a = random.randint(0,i)
    b = random.randint(0,i)
    start_time = time.time()
    my_gcd(a,b)
    T_pgcd.append(time.time() - start_time)
    i += 1000000000000000000000000000000000000000000000000000

plt.plot(x, T_pgcd)
plt.show()



T_pgcd = []
T_inverse = []

i = 10
x = []

while i < 100000000000000000000000000000000000000000000000000000:
#for b in [10**5, 10**10, 10**15, 10**20, 10**25]:
    x.append(i)
    a = random.randint(0,i)
    b = random.randint(0,i)
    start_time = time.time()
    my_inverse(a,b)
    T_pgcd.append(time.time() - start_time)
    i += 1000000000000000000000000000000000000000000000000000

plt.plot(x, T_pgcd)
plt.show()




#k = np.argmax(T_pgcd)
#print(x[k], T_pgcd[k])

#print(table(5))x
#print(my_inverse(11,3))"""
