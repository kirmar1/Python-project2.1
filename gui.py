from tkinter import *
from tkinter import messagebox
import serial


serialArduino = serial.Serial('COM3', 9600)

#create window
root = Tk()

#modify root window
root.title ("Python")#label
root.geometry("1000x600")# size

label = Label( text = "Status:") #label
label.place(x=50, y=5) #puts label on screen

#variable
y2 = 0
var1 = getValueLicht()
var2 = 12
uur = 0
Y2tijdelijk = 400
knipperTemp = True
grafiek = True
yAsVar = 150
yAsBerekenen = 0.33
huidige_ondergrens = 600
huidige_bovengrens = 800
huidige_bovengrenst = 22
huidige_ondergrenst = 20
saveValueLicht = 0
saveValueTemp = 0
statusinput = 1

def getValueLicht():
    valueRead = serialArduino.readline()
    if 'L' in str(valueRead):
        value = getValueOfArduino()
        if value is None:
            global saveValueLicht
            print('Save Value word geprint',saveValueLicht )
            return saveValueLicht
        else:
            global saveValueLicht
            saveValueLicht = value
            print('value return',value )
            return saveValueLicht
    elif 'T' in str(valueRead):
        value = getValueOfArduino()
        print(value,'geen licht')
        saveValueLicht = 0
        return 0
    elif 'S' in str(valueRead):
        print(str(valueRead))
        value = getValueOfArduino()
        if value == 0:
            Status(1)
        elif value == 1:
            Status(3)
        else:
            print("pizza")
        print (value,"dit is geen temp maar een s return saveValueLicht =", saveValueLicht)
        global saveValueLicht
        return saveValueLicht
    elif 'A':
        Status(2)
        value = getValueOfArduino()
        if value is None:
            return value
        else:
            return saveValueLicht
    else:
        print('check getValueLicht')

def getValueTemp():
    valueRead = serialArduino.readline()
    if 'L' in str(valueRead):
        print(str(valueRead))
        value = getValueOfArduino()
        print (value,"dit is geen temp")
        saveValueTemp = 0
        return 0

    elif 'T' in str(valueRead):
        print(str(valueRead))
        value = getValueOfArduino()
        print(value, 'value')
        if value is None:
            global saveValueTemp
            print('Save Value return',saveValueTemp )
            return saveValueTemp
        else:
            global saveValueTemp
            saveValueTemp = value
            print('value return',value )
            return value
    elif 'S' in str(valueRead):
        print(str(valueRead))
        value = getValueOfArduino()
        if value == 0:
            Status(1)
        elif value == 1:
            Status(3)
        print (value,"dit is geen temp maar een s return saveValueTemp =", saveValueTemp)
        global saveValueTemp
        return  saveValueTemp
    elif 'A':
        Status(2)
        return saveValueTemp
    else:
        print('check getValueTemp')

def getValueOfArduino():
    valueRead = serialArduino.readline()
    valueInInt = int(valueRead)
    print(valueInInt)
    return valueInInt




#grafiek

canvas = Canvas(root, width=800, height=500, bg='white')
canvas.place(x=10, y=30)

canvas.create_line(50, 400, 765, 400, width=2)  # x-axis    (afstand rand, begin, lengte, einde)
canvas.create_line(50, 400, 50, 50, width=2)  # y-axis  (afstand rand onder , lengte lijn ,boven links  , lengte van af boven)

# x-axis
for i in range(24):
    x = 50 + (i * 30)
    canvas.create_line(x, 400, x, 50, width=1, dash=(2, 5))
    canvas.create_text(x, 410, text='%d' % (1 * i), anchor=N)

# y-axis
def yAs(yAsVar):
    for i in range(8):
        y = 400 - (i * 50)
        canvas.create_line(50, y, 750, y, width=1, dash=(2, 5), tags='ytemp')
        canvas.create_text(40, y, text='%d' % (yAsVar * i), anchor=E, tags='ytemp')


#layout functie's
def button(xTemp, yTemp,text,command):
    button = Button(text=text, width=18, command=command)
    button.place(x=xTemp, y=yTemp)

def buttonKlein(xTemp, yTemp,text,command):
    button = Button(text=text, width=6, command=command)
    button.place(x=xTemp, y=yTemp)

def label():
    label_test = Label( text="De label_test")  # label
    label_test.place(x=250, y=5)  # puts label on screen

def newGrafiek():
    global grafiek, yAsVarBer
    if grafiek == True:
        grafiek = False
        canvas.delete('ytemp')
        yAs(5)
        yAsVarBer = 10
    elif grafiek == False:
        grafiek = True
        canvas.delete('ytemp')
        yAs(150)
        yAsVarBer = 0.33
    else:
        print('kijk naar functie newGrafiek')

def newTempGrafiek():
    global  yAsVarBer, grafiek
    canvas.delete('ytemp')
    yAs(5)
    yAsVarBer = 10
    grafiek = False

def newLichtGrafiek():
    global yAsVarBer, grafiek
    canvas.delete('ytemp')
    yAs(150)
    yAsVarBer = 0.33
    grafiek = True

def set_open():
    open =("I"+1)
    print(open)
    serialArduino.write(open.encode())

def set_dicht():
    dicht =("I"+0)
    print(dicht)
    serialArduino.write(dicht.encode())

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
    if len(txt_boven.get()) != 0:
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

def set_ondert():
    if len(txt_onder.get()) != 0:
        ondergrens = int(txt_ondert.get())
        if ondergrens < huidige_bovengrenst:
            global huidige_ondergrenst
            huidige_ondergrenst = ondergrens
            ondergrens_tosend = ("K" + str(ondergrens))
            print(ondergrens_tosend)
            serialArduino.write(ondergrens_tosend.encode())
        else:
            messagebox.showerror('Input error', 'Ondergrens ligt boven de bovengrens')
    else:
        messagebox.showerror('Input error', 'Voer een geldige waarde in')

def set_bovent():
    if len(txt_boven.get()) != 0:
        bovengrens = int(txt_bovent.get())
        if bovengrens > huidige_ondergrenst:
            global huidige_bovengrenst
            huidige_bovengrenst = bovengrens
            bovengrens_tosend = ("H" + str(bovengrens))
            print(bovengrens_tosend)
            serialArduino.write(bovengrens_tosend.encode())
        else:
            messagebox.showerror('Input error', 'Bovengrens ligt onder de ondergrens')
    else:
        messagebox.showerror('Input error', 'Voer een geldige waarde in')

#lijn functie
def lijn():
    global uur,y2 ,var1, Y2tijdelijk, grafiek
    if uur == 23:
        canvas.delete('temp')
        uur = 0
    Tijdtemp = uur
    x1 = 50 + (Tijdtemp * 30)  # begin op de x as 50 ==0
    y1 = Y2tijdelijk  # hogte op de y ass begin 400 ==0
    Tijdtemp = uur
    x2 = 80 + (Tijdtemp * 30)  # einde lijn schuin 50 == 0
    y2 = 400 - (var1 * yAsBerekenen)  # lengte lijn 400 ==0
    Y2tijdelijk = y2
    canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
    uur += 1
    var1 = getValueLicht()
    if grafiek == True:
        canvas.after(300, lijn)
    elif grafiek == False:
        canvas.after(300, lijn2)
        canvas.delete('temp')
        uur = 0
    else:
        print('kijk naar functie lijn')

    # lijn

def lijn2():
    global uur, y2, var2, Y2tijdelijk, grafiek
    if uur == 23:
            canvas.delete('temp')
            uur = 0
    Tijdtemp = uur
    x1 = 50 + (Tijdtemp * 30)  # begin op de x as 50 ==0
    y1 = Y2tijdelijk  # hogte op de y ass begin 400 ==0
    Tijdtemp = uur
    x2 = 80 + (Tijdtemp * 30)  # einde lijn schuin 50 == 0
    y2 = 400 - (var2 * 10)  # lengte lijn 400 ==0
    Y2tijdelijk = y2
    canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
    uur += 1
    var2 = getValueTemp()
    if grafiek == False:
        canvas.after(300, lijn2)
    elif grafiek == True:
        canvas.after(300, lijn)
        canvas.delete('temp')
        uur = 0
    else:
        print('kijk naar functie lijn2')

#status lampjes aanmaken

def led(xTemp, collor,reload,functie):
    canvas2 = Canvas(root, width=20, height=20, bg=collor)
    canvas2.place(x=xTemp, y=5)
    if reload == True:
        canvas2.after(300, functie)

#geeft de status waar het scherm zich in bevind
def Status(status):
    if status == 1:
        tekst = "Dicht"
    elif status == 2:
        tekst = "In/uit rollen"
    elif status == 3:
        tekst = "Open"
    else:
        print('Dit gaat fout check status')
    label = Label(text=tekst)  # label
    label.place(x=100, y=5)

# label Boven status
label = Label(text="Status:")  # label
label.place(x=50, y=5)  # puts label on screen

#buttons nieuwe grafiek
button(840, 30, 'Temperatuur grafiek',newTempGrafiek)
button(840, 70, 'Licht grafiek',newLichtGrafiek)

# label Configiratie scherm
label = Label( text = "Configuratie: Scherm") #label
label.place(x=840, y=120) #puts label on screen

buttonKlein(840,145, 'Open',set_open)
buttonKlein(920,145, 'Dicht',set_dicht)

# label Configiratie temperatuur
label = Label( text = "Configuratie: Temperatuur") #label
label.place(x=840, y=195) #puts label on screen

#input voor de ondergrens van de temperatuur
label_ondert = Label(text="Ondergrens:")
label_ondert.place(x=820,y=220)
txt_ondert = Entry(root)
txt_ondert.insert(0,huidige_ondergrenst)
txt_ondert.place(x=820,y=240)
btnSetMaxMint = Button(root, text="Set", command=set_ondert)
btnSetMaxMint.place(x=960, y=234)

#input voor de bovengrens van de temperatuur
label_bovent = Label(text="Bovengrens:")
label_bovent.place(x=820,y=260)
txt_bovent = Entry(root)
txt_bovent.insert(0,huidige_bovengrenst)
txt_bovent.place(x=820, y=280)
btnSetMaxMint = Button(root, text="Set", command=set_bovent)
btnSetMaxMint.place(x=960, y=276)

# label Configiratie licht
label = Label( text = "Configuratie: Licht") #label
label.place(x=840, y=315) #puts label on screen

#input voor de ondergrens van het licht
label_onder = Label(text="Ondergrens:")
label_onder.place(x=820,y=335)
txt_onder = Entry(root)
txt_onder.insert(0,huidige_ondergrens)
txt_onder.place(x=820,y=355)
btnSetMaxMin = Button(root, text="Set", command=set_onder)
btnSetMaxMin.place(x=960, y=351)

#input voor de bovengrens van het licht
label_boven = Label(text="Bovengrens:")
label_boven.place(x=820,y=375)
txt_boven = Entry(root)
txt_boven.insert(0,huidige_bovengrens)
txt_boven.place(x=820, y=395)
btnSetMaxMin = Button(root, text="Set", command=set_boven)
btnSetMaxMin.place(x=960, y=391)

#kick off event loop
yAs(150)
lijn()
root.mainloop()