#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:03:16 2018

@author: 3522144
"""
import math
import time
import random

'''
import numpy as np
import matplotlib.pyplot as plt
import time
import random
from math import *
'''


#https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def my_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

def all_inverse(n):
	l=[]
	for i in range(n):
		if my_inverse(i,n) != -1:
			l.append(i)
	return l

def my_gcd(a,b) :
    if (b==0) :
        return(a)
    else :
        r=a%b
        return my_gcd(b,r)


def my_expo_mod(base, exponent, modulus):
    result=1
    while (exponent > 0):
       # print(exponent)
        if ((exponent & 1) > 0):
            result = (result * base)%modulus
        exponent >>= 1
        base = (base * base)%modulus
    return result


def first_test(n):
    if n<7:
        if n in (2,3,5):
            return True
        else:
            return False
    if n & 1 == 0:
        return False
    k=3
    r=math.sqrt(n)
    while k<=r:
        if n % k == 0:
            return False
        k+=2
    return True


def is_carmichael_naive(N):
    if N == 0 or N == 1:
        return False
    if first_test(N):
        return False
    for j in range(2,N):
        if my_gcd(j,N) == 1:
            if my_expo_mod(j,N-1,N) != 1:
                
                return False
    return True

'''cpt=0
for i in range(0,100000  ):
    if estpremier(i):
        cpt = cpt + 1'''

def liste_premiers(n):
	l = []
	for i in range(0,n):
		if first_test(i):
			l.append(i)
			
	return l 
	
	
def gen_carmichael(n, b_time=False):
	l = []
	if not b_time:
		for i in range(n):
			if is_carmichael_naive(i):
				l.append(i)
	else:
		start_time = time.time()
		i = 0
		
		while True:
			if is_carmichael_naive(i):
				l.append(i)
				print(i)
			t = time.time() - start_time
			
			if t >= 3000:
				break
			i += 1
			
	return l
	
def trois_qr():
	carm = gen_carmichael(1000, False)
	for i in carm:
		if (i%3 == 0):
			 p = 3
			 h = 2
			 r = (i-1+h)/h
			 q = i/(3*r)
			 print(str(p) + '*' + str(q) + '*' + str(r) + "=" + str(i))

"""   
def miller_rabin(n):
	
	if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
		return False
	if n==2 or n==3 or n==5 or n==7:
		return True
		
	h = 0
	m = n-1
	bon = True
	T = 8
	
	while m%2==0:
		m>>=1
		h+=1
		
	for i in range(T):
		a = random.randrange(2, n)
		bon = True
		if pow(a, m, n) == 1:
			bon = False
		else:
			for i in range(m):
				if pow(a, 2**i * m, n) == n-1:
					bon = False
		if bon:
			return False
	return True
        
 
print(miller_rabin(651))"""



def miller_rabin(n):
		
	h = 0
	m = n-1
	bon = True
	T = 5
	
	while m%2==0:
		m>>=1
		h+=1
	print(m)
	print(h)
	
	for i in range(T):
		inverses = all_inverse(n)
		x = random.randrange(0, len(inverses))
		a = inverses[x]
		b = my_expo_mod(a,m,n)
		print("b "+str(b))
		if b!=1 and b != n-1:
			#print("o")
			for j in range(1,h):
				print(h)
				if b!= n-1 and my_expo_mod(b,2,n) == 1:
					return False
			b = my_expo_mod(b,2,n)
		if b != n-1:
			print("o")
			return False		
	return True
        
print(miller_rabin(17))

def fonc2(a,n):
    """int->int
    calcul a^(n-1)% n sans calculer a^(n-1)  """
    k=1
    i=0

    while i<n-1:
         k=(k*a)%n
         i=i+1
    return k

def fonc3(a,n,p):
    """int->int
    calcul a^(n-1)% n sans calculer  a^((n-1)/p)%n"""
    k=1
    i=0

    while (i<(n-1)//p):
        k=(k*a)%n
        i=i+1
    return k

def pgcd(a,b):
    """int->int
    pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)
     
def reciproqueFermat(n):
    """int->bool
    la réciproque de theroem de Fermat nous dit que l'entier n est premier si:
    si il existe un a appartenant à premier à n tel que on a:
    a^(n-1)%n =1 et a^((n-1)/p)%n!=1 ∀ p telque (n-1)%p=0
    la fonction renvoit True si le nombre est premier ,False si non."""

    m=0
    s=0
    g=0
    L=[]
    x=0
    M=[]
    e=1

    if n==1:
         return False
    elif n%2==0 and n!=2:
        return False
    elif n==2:
        return True

    else:
        while e<n:             #On construit l'ensemble M contenant tous les a telque a est premier à n.
            if pgcd(e,n)==1:
                M.append(e)
            e=e+1

        for x in range (2,n):  #On construit l'ensemble L contenant tous les p telque (n-1)%p=0.
            if n-1%x==0:
                L.append(x)
    
    
        while s<len(L) :       #On verifie la premeir condition si c'est le cas on verifie la suite si non on renvoit False.
            while g<len(M):
                if fonc3(M[g],n,L[s])!=1:
                    g=g+1
                    s=s+1
                else:
                    return False
        g=0
        while g<len(M):        #On verifie la deuxiem condition on renvoie True si c'est le cas ,False si non.
            if fonc2(M[g],n)==1:
                g=g+1
            else:
                return False
            
        

    return True
    

def test_fermat(N):
	a = 2
	b = my_expo_mod(a, N, N)
	if (b-a) % N == 0:
		return True # possiblement premier
	else:
		return False # premier

def pe_test_fermat():
	n = 1000
	premiers = liste_premiers(n)
	pseudo_premiers = []
	
	err = 0
	
	for i in range(2,n):
		#b = reciproqueFermat(i)
		b = test_fermat(i)
		if b and i not in premiers:
			err += 1
			pseudo_premiers.append(i)
			
	return (err / (n-2), premiers, pseudo_premiers)

'''
def qr(p):

	for h in range(1, p):
		for d in range(0, h+p):
			if (h + p)*(p-1) % d == 0 and -p 

	for 1 < h3 < Prime1
		for 0 < d < h3+Prime1
		     if (h3+Prime1)*(Prime1-1) mod d == 0 and -Prime1 squared mod h3 == d mod h3
		     then
		           Prime2 = 1 + ((Prime1-1) * (h3+Prime1)/d)
		           next d if Prime2 is not prime
		           Prime3 = 1 + (Prime1*Prime2/h3)
		           next d if Prime3 is not prime
		           next d if (Prime2*Prime3) mod (Prime1-1) not equal 1
		           Prime1 * Prime2 * Prime3 is a Carmichael Number


def carmichael_tuple(p1):
    ans = []
    if isprime(p1):
        for h3 in range(2, p1):
            g = h3 + p1
            for d in range(1, g):
                if (g * (p1 - 1)) % d == 0 and (-p1 * p1) % h3 == d % h3:
                    p2 = 1 + ((p1 - 1)* g // d)
                    if isprime(p2):
                        p3 = 1 + (p1 * p2 // h3)
                        if isprime(p3):
                            if (p2 * p3) % (p1 - 1) == 1:
                                #print('%i X %i X %i' % (p1, p2, p3))
                                ans += [tuple(sorted((p1, p2, p3)))]
    return ans
'''
#print("réciproque fermat : {}".format(reciproqueFermat(2464)))
#print(gen_carmichael(10**5))
#print(gen_carmichael(10**5, True))

res = pe_test_fermat()
#print("Probabilité d'erreur : {}".format(res[0]))
#print("Nombres premiers : {}".format(res[1]))
#print("Nombres pseudo-premiers : {}".format(res[2]))

#print("test fermat : {}".format(test_fermat(2464)))
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
