import math

class Figur:
    """
    Basisklasse fuer geometrische Figuren
    mit Laenge x Breite
    """
    def __init__(self, br = 5, le = 10):
        self.breite = br
        self.laenge = le

    def zeige_werte(self):
        """ Abmessungen ausgeben """
        print("Breite =", self.breite, "Laenge =", self.laenge)

class Rechteck(Figur):
    """ Von Figur abgeleitete Klasse Rechteck """
    def flaeche(self):
        print("Flaeche Rechteck =", self.breite * self.laenge)

class Ellipse(Figur):
    """ Von Figur abgeleitete Klasse Ellipse """
    def flaeche(self):
        print("Flaeche Ellipse =",  round(self.breite * self.laenge * math.pi, 2))
        

def main():
    x = Rechteck(3, 4)
    y = Ellipse(7, 3)
    
    figuren_liste = []
    figuren_liste.append(x)
    figuren_liste.append(y)
    figuren_liste.append(Ellipse(3, 3))
    figuren_liste.append(Rechteck())

    for fig in figuren_liste:
        fig.zeige_werte()
        fig.flaeche()
    

if __name__ == "__main__":
    main()
    
