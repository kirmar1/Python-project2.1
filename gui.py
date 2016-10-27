from tkinter import *

def label_test():
    label_test = Label(app, text="De label_test")  # label
    label_test.grid()  # puts label on screen

#creat window
root = Tk()

#modify root window
root.title ("Centrale")#label bovenaan scherm
root.geometry("1000x600")# size

#labels
app = Frame(root)
app.grid()#puts app in screen

label = Label(app, text = "De label") #label
label.grid() #puts label on screen

#buttons
button1 = Button(text = "Button", width=10, command=label_test)
button1.place(x=890, y=0)

button2 = Button(text = "Button2", width=10)
button2.place(x=890, y=30)

#grafiek

canvas = Canvas(root, width=800, height=500, bg='white')
canvas.place(x=10, y=30)

canvas.create_line(50, 400, 750, 400, width=2)  # x-axis    (afstand rand, begin, lengte, einde)
canvas.create_line(50, 400, 50, 50, width=2)  # y-axis  (afstand rand onder , lengte lijn ,boven links  , lengte van af boven)


# x-axis
for i in range(15):
    x = 50 + (i * 50)
    canvas.create_line(x, 400, x, 50, width=1, dash=(2, 5))
    canvas.create_text(x, 410, text='%d' % (10 * i), anchor=N)

# y-axis
for i in range(8):
    y = 400 - (i * 50)
    canvas.create_line(50, y, 750, y, width=1, dash=(2, 5))
    canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)


#kick off event loop

root.mainloop()


