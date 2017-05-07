#!/usr/bin/env python3

from random import *
x = randint(1, 100)

rate = 0
while rate != x:
    rate = int(input("Zahl: "))
    if (rate > x):
        print("zu hoch")
    elif rate < x:
        print("zu niedrig")
               
    
print("Fertig!")
