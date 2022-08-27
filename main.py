from tkinter import *
import random

Lottery = Tk()
Lottery.geometry('800x360')
Lottery.resizable(0, 0)
Lottery.title("Lottery")

def draw_numbers():
   random_numbers = random.sample(range(1, 31), 6)
   random_numbers.sort()
   text.config(text = random_numbers)

##COMPUTER INPUT
var = StringVar()
var.set("Lottery numbers")
frame1 = Frame(Lottery)
frame1.pack(side=TOP)

label = Label(frame1, textvariable=var, font =("Arial", 24), width=20)
label.pack(side=TOP)

##COMPUTER NUMBERS
button = Button(frame1, text = "Draw numbers", width = 25, command = draw_numbers)
button.pack(padx = 1, pady = 1)

text = Label(frame1, text = random.sample(range(1, 31), 6))
text.pack(padx = 0, pady = 1)

##USER INPUT
frame2 = Frame(Lottery)
var = StringVar()
var.set("Choose 6 numbers between 1 - 30.")
frame2 = Frame(Lottery)
frame2.pack(side=TOP)

label = Label(frame1, textvariable=var, font
=("Arial", 24), width=70)
label.pack(side=TOP)

#USER NUMBERS
frame2.pack(side=TOP)
txtDisplay = Entry(frame2, bd=20, insertwidth=1, font=("Arial", 24), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, bd=20, insertwidth=1, font=("Arial", 24), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, bd=20, insertwidth=1, font=("Arial", 24), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, bd=20, insertwidth=1, font=("Arial", 24), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, bd=20, insertwidth=1, font=("Arial", 24), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, bd=20, insertwidth=1, font=("Arial", 24), justify='center', width=4)
txtDisplay.pack(side=LEFT)

Lottery.mainloop()