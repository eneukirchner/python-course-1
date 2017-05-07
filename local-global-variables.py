#!/usr/bin/env python3
# Globale und lokale Variablen, Namensräume
def myfunc1():
    text = "innen"

def myfunc2():
    global text
    text = "innen"
    
def myfunc3():
    myfunc3.text = "innen"

def myfunc4():
    text = text + "innen"
    
text = "aussen"
myfunc3.text = "aussen"

myfunc1()
print("myfunc1 liefert: " + text)

myfunc2()
print("myfunc2 liefert: " + text)

myfunc3()
print("myfunc3 liefert: " + myfunc3.text)

# geht nicht:
# myfunc4()
# print("myfunc4 liefert: " + myfunc4.text)
