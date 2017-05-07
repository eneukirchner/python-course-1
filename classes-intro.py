#!/usr/bin/env python3
import math

# Klassendefinition
class Shape:
    # Konstruktor
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # print(self)

    # Methode
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

# Abgeleitete Klasse
class Rectangle(Shape):
    def area(self):
        print("Fläche Rechteck = ", round(self.width * self.height, 2))
        

class Ellipse(Shape):
    def area(self):
        print("Fläche Ellipse = ", round(self.width * self.height * math.pi, 2))


# Objekte: r1, e1
r1 = Rectangle(4, 5)
r1.area()

r1.set_dimensions(40, 50)
r1.area()

e1 = Ellipse(10, 100)
e1.area()

# Objekterstellung und Anwendung einer Methode als Einzeiler
Rectangle(2, 3).area()
