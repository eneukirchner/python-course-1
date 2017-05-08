#!/usr/bin/env python3
# pi-benchmark.py
import random
import math
import time

STEPS = 100000
n = 0
i = 0

start = time.clock()
while n < STEPS:
    x = random.random()
    y = random.random()
    r = math.sqrt(x**2 + y**2)
    if r < 1:
        i += 1
    n += 1

pi = 4*i/n
stop = time.clock()
print("Pi = ", pi, " n = ", n, " Zeit = ", round(stop - start, 4))

        
    


