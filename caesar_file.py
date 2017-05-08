#!/usr/bin/env python3
import caesar

alphabet="abcdefghijklmnopqrstuvwxyz"
key = int(input("Schlüssel: "))

f = open('nachricht.txt', encoding = 'utf-8')
for line in f:
    print(caesar.caesar(line, key, alphabet))
f.close()

input("Enter zum Beenden")
