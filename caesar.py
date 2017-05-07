#!/usr/bin/env python3
def caesar(ein, schluessel, abc):
    ein = ein.lower()
    aus = ""
    for buchstabe in ein:
        pos = abc.find(buchstabe)
        neu = (pos + schluessel) % len(abc)
        if pos > 0:
            verschluesselt = abc[neu]
        else:
            verschluesselt = buchstabe
        aus += verschluesselt
    return aus
    
if __name__ == "__main__":
    alphabet="abcdefghijklmnopqrstuvwxyz"
    text = input("verschlüssle Text: ")
    key = int(input("Schlüssel: "))
    print(caesar(text, key, alphabet))
    input("Enter zum Beenden")
