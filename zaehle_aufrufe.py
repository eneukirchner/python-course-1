# Definiere die Funktion:
def zaehle():
    """
    Die Funktion gibt mittels print aus, wie oft sie
    aufgerufen wurde.
    Statische Variable zaehle.n
    """
    zaehle.n += 1
    print("Ich wurde", zaehle.n, "mal aufgerufen")
    
# Aufrufe:
if __name__ == "__main__":
    zaehle.n = 0
    zaehle()
    zaehle()
    zaehle()



