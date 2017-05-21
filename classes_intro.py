#!/usr/bin/env python3
import math
"""
    Geometrical Shapes
"""
class Shape:
    """
    Base Class for all shapes
    """
    def __init__(self, w = 5, l = 3):
        self.width = w
        self.length = l

    def show(self):
        print("Width =", self.width, "Length =", self.length)

    def set(self, w, l):
        self.width = w
        self.length = l

class Rectangle(Shape):
    """
    Rectangle Class
    """
    def area(self):
        print("Area Rectangle =", self.width * self.length)

class Ellipse(Shape):
    """
    Ellipse Class
    """
    def area(self):
        print("Area Ellipse =", round(self.width * self.length * math.pi, 2))

def main():
    shape_list = []
    shape_list.append(Rectangle(10, 5))
    shape_list.append(Rectangle(2, 4))
    shape_list.append(Ellipse(10, 3))

    for shape in shape_list:
        shape.show()
        shape.area()

if __name__ == "__main__":
    main()




    


        
        
