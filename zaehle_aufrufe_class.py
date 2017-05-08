#!/usr/bin/env python3

# Klassendefinition
class Zaehle:
    """
    Inkrementiere oder dekrementiere ein Objekt
    Zaehle()...erzeuge Objekt mit Startwert 0
    Zaehle(5)... erzeuge Objekt mit Startwert 5
    increment() ... Zunahme um 1
    increment(2)... Zunahme um 2
    decrement() ... Abnahme um 1
    decrement(2)... Abnahme um 2
    """
    
    # Konstruktor
    def __init__(self, i = 0):
        self.i = i
        
    # Methoden
    def increment(self, n = 1):
        self.i += n
        print(self.i)

    def decrement(self, n = 1):
        self.i -= n
        print(self.i)

# Objekte:
if __name__ == "__main__":
    x = Zaehle()
    x.increment()
    x.increment()
    x.decrement()
    x.increment(5)

    y = Zaehle(10)
    y.increment()



