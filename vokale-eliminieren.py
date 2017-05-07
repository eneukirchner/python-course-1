#!/usr/bin/env python3
def elim_vok(txt, vok):
    out = ""
    for b in txt:
        if vok.find(b.lower()) < 0:
            out += b
    return out
            
vokale = "aeiouäöü"
fh = open("nachricht.txt")
for zeile in fh:
    print(elim_vok(zeile, vokale))
fh.close()
