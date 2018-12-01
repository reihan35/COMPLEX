#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import matplotlib.pyplot as plt
import utils

T_pgcd = []
T_inverse = []

i = 10
x = []

while i < 100000000000000000000000000000000000000000000000000000:
    x.append(i)
    a = random.randint(0,i)
    b = random.randint(0,i)
    start_time = time.time()
    utils.my_gcd(a,b)
    T_pgcd.append(time.time() - start_time)
    i += 1000000000000000000000000000000000000000000000000000

plt.plot(x, T_pgcd)
plt.show()

T_pgcd = []
T_inverse = []

i = 10
x = []

while i < 100000000000000000000000000000000000000000000000000000:
    x.append(i)
    a = random.randint(0,i)
    b = random.randint(0,i)
    start_time = time.time()
    utils.my_inverse(a,b)
    T_pgcd.append(time.time() - start_time)
    i += 1000000000000000000000000000000000000000000000000000

plt.plot(x, T_pgcd)
plt.show()
