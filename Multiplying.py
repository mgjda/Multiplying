#!/usr/bin/env python
"""Multiplying.py: Multiplying two digits from 1 to 9 to training or learing.
The app shows two random digits, user enter a result of multiplying of these."""

__author__ = "mgjda"

#import tkinter library
from tkinter import *
import random

#size of window
HEIGHT = 300
WIDTH = 300

#create main window
window = Tk()
window.title("Multiplying")

#variables
vara = StringVar()
varb = StringVar()
varx = StringVar()
a = random.randint(1,9)
b = random.randint(1,9)

#methods

#setting random numbers for variables and labels
def randomNumbers(x, y):
   x = random.randint(1,9)
   y = random.randint(1,9)
   vara.set(x)
   varb.set(y)
   global a, b
   a = x
   b = y

#checking if entry input is the same as result
def checkIt(entry, x, y):
	if int(entry.get()) == x * y:
		entry.delete(0,END)
		randomNumbers(x,y)
	else:
		print("None")

#canvas
canvas = Canvas(window, height = HEIGHT, width = WIDTH)
canvas.pack()

#background image setting bg (This image is from https://www.toptal.com/designers/subtlepatterns/)
background_image = PhotoImage(file='email-pattern.png')
background_label = Label(window, image=background_image)
background_label.place(relwidth = 1, relheight = 1)

#labels and setting position in window
la = Label( window, textvariable=vara, relief=RAISED, font = "Helvetica 30 bold", bd = 0)
la.place(relx = 0.05, rely = 0.15, relwidth = 0.25, relheight = 0.25)

lb = Label( window, textvariable=varb, relief=RAISED, font = "Helvetica 30 bold", bd = 0 )
lb.place(relx = 0.7, rely = 0.15, relwidth = 0.25, relheight = 0.25)

lx = Label( window, textvariable=varx, relief=RAISED, font = "Helvetica 30 bold", bd = 0 )
lx.place(relx = 0.375, rely = 0.15, relwidth = 0.25, relheight = 0.25)

#setting
vara.set(a)
varb.set(b)
varx.set("x")

#entry is an input
entry = Entry(window, bd = 5, font = "Helvetica 30 bold", justify = CENTER)
entry.insert(END, '0') #default = '0'
entry.focus_set() #focus on app start
entry.place(relx = 0.2, rely = 0.55, relwidth = 0.4, relheight = 0.25)

#button use to check result
button = Button(window, text ="ok", font = "Helvetica 20 bold", command = lambda: checkIt(entry,a,b))
button.place(relx = 0.6, rely = 0.55, relwidth = 0.25, relheight = 0.25)

#bind 'ENTER' key to check result **NOT WORKING**
window.bind('<Return>', checkIt(entry,a,b))

#looping main window
window.mainloop()