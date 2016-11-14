from tkinter import *
from tkinter import messagebox
import serial
import time

serialArduino = serial.Serial('COM3', 9600)

huidige_ondergrens = 600
huidige_bovengrens = 800

def makeTkEntry(parent, label, width=None, **options):
    Label(parent, text=label).pack()
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack()
    return entry


def set_onder():
    if len(txt_onder.get()) != 0:
        ondergrens = int(txt_onder.get())
        if ondergrens < huidige_bovengrens:
            global huidige_ondergrens
            huidige_ondergrens = ondergrens
            ondergrens_tosend =("O"+str(ondergrens))
            print(ondergrens_tosend)
            serialArduino.write(ondergrens_tosend.encode())
        else:
            messagebox.showerror('Input error', 'Ondergrens ligt boven de bovengrens')
    else:
        messagebox.showerror('Input error', 'Voer een geldige waarde in')

def set_boven():
    if len(txt_onder.get()) != 0:
        bovengrens = int(txt_boven.get())
        if bovengrens > huidige_ondergrens:
            global huidige_bovengrens
            huidige_bovengrens = bovengrens
            bovengrens_tosend =("B"+str(bovengrens))
            print(bovengrens_tosend)
            serialArduino.write(bovengrens_tosend.encode())
        else:
            messagebox.showerror('Input error', 'Bovengrens ligt onder de ondergrens')
    else:
        messagebox.showerror('Input error', 'Voer een geldige waarde in')





guiRoot = Tk()
guiRoot.title('input test gui')

guiControlsFrame = Frame(guiRoot, width=200, borderwidth=5)
guiControlsFrame.pack()

txt_onder = makeTkEntry(guiControlsFrame, "Ondergrens:", 20)
txt_onder.insert(0,huidige_ondergrens)
txt_onder.pack()
btnSetMaxMin = Button(guiControlsFrame, text="Set ondergrens", command=set_onder)
btnSetMaxMin.pack()
txt_boven = makeTkEntry(guiControlsFrame, "Bovengrens:", 20)
txt_boven.insert(0,huidige_bovengrens)
txt_boven.pack()
btnSetMaxMin = Button(guiControlsFrame, text="Set bovengrens", command=set_boven)
btnSetMaxMin.pack()


guiRoot.mainloop()