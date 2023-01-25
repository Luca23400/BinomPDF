import math
import tkinter 

def quad():
    print("button wurde gedrückt")
    wert  = eingabeFeld.get()
    print(wert)
    zahl = int (wert)
    quadrat = zahl*zahl
    ausgabeLabel = tkinter.Label(fenster,text=quadrat)
    ausgabeLabel.pack()

fenster = tkinter.Tk()
eingabeaufforderung = tkinter.Label(fenster,text = "Geben sie eine zu prüfende Zahl ein: ")
eingabeFeld = tkinter.Entry(fenster)
eingabeButton = tkinter.Button(fenster,text ="Eingabe",command = quad)

eingabeaufforderung.pack()
eingabeFeld.pack()
eingabeButton.pack()
fenster.mainloop()