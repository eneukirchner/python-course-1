#!/usr/bin/env python3
def zaehle(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for buchstabe in text:
        buchstabe = buchstabe.lower()
        
        # nur Buchstaben aus alphabet zaehlen
        if alphabet.find(buchstabe) < 0:
            continue
        
        if buchstabe in zaehle.zahl:
            zaehle.zahl[buchstabe] += 1 
        else:
            # Zahl fuer diesen Buchstaben noch nicht
            # definiert
            zaehle.zahl[buchstabe] = 1

if __name__ == "__main__":            
    zaehle.zahl = {}
    f = open('nachricht.txt', encoding = 'utf-8')
    for line in f:
        zaehle(line)
    f.close()
    maximum = 0
    for b in zaehle.zahl:
        print(b + " -> " + str(zaehle.zahl[b]))
        if zaehle.zahl[b] > maximum:
            maximum = zaehle.zahl[b]
            sieger = b
    print("Häufigster Buchstabe: " + sieger + " -> " + str(maximum))
