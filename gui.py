from tkinter import *
from random import randint

#creat window
root = Tk()

#groote en naam window 'root'
root.title ("Python")#label
root.geometry("1000x600")# size


#variable
y2 = 0
var1 = 15
var2 = 12
uur = 0
Y2tijdelijk = 400
knipperTemp = True
grafiek = True

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
for i in range(8):
    y = 400 - (i * 50)
    canvas.create_line(50, y, 750, y, width=1, dash=(2, 5))
    canvas.create_text(40, y, text='%d' % (5 * i), anchor=E)

#layout functie's
def button(xTemp, yTemp,text,command):
    button = Button(text=text, width=10, command=command)
    button.place(x=xTemp, y=yTemp)
def label():
    label_test = Label( text="De label_test")  # label
    label_test.place(x=250, y=5)  # puts label on screen
def newGrafiek():
    global grafiek
    if grafiek == True:
        grafiek = False
    elif grafiek == False:
        grafiek = True
    else:
        print('kijk naar functie newGrafiek')

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
    y2 = 400 - (var1 * 10)  # lengte lijn 400 ==0
    Y2tijdelijk = y2
    canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
    print(uur, x1, y1, x2, y2, var1)
    uur += 1
    var1 = randint(0, 35)
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
    print(uur, x1, y1, x2, y2, var2)
    uur += 1
    var2 = randint(0, 35)
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
def knipper():
    global knipperTemp
    led(100,'white',False,knipper)  # eerste led
    led(180,'white',False,knipper)  # derde led
    print(knipperTemp)
    # tweed led yellow knipperen
    if knipperTemp == True:
        led(140,'yellow',True,knipper)
        knipperTemp = False
    else:
        led(140,'white',True,knipper)
        knipperTemp = True
def groen():
    led(100, 'green', True, groen) # eerste led
    led(140,'white',False,groen)  # tweede led
    led(180,'white',False,groen)  # derde led
def rood():
    led(100, 'white', False, rood) # eerste led
    led(140,'white',False,rood)  # tweede led
    led(180,'red',True,rood)  # derde led
#geeft de status waar het scherm zich in bevind
def Status(status):
    if status == 1:
        groen()
    elif status == 2:
        knipper()
    elif status == 3:
        rood()
    else:
        print('Dit gaat fout check status')

#buttons
button(890, 0, 'hallo',label)
button(890, 60, 'newGrafiek',newGrafiek)
#labels
label = Label( text = "Status:") #label
label.place(x=50, y=5) #puts label on screen


#kick off event loop
Status(1)
lijn()
root.mainloop()
