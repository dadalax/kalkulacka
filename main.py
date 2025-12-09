import math
from tkinter import *

root = Tk()
root.geometry('230x250')

buffer = ""
def defone():
    global buffer
    buffer +="1"
    updateLabel()
def deftwo():
    global buffer
    buffer += "2"
    updateLabel()
def defthree():
    global buffer
    buffer += "3"
    updateLabel()
def deffour():
    global buffer
    buffer += "4"
    updateLabel()
def deffive():
    global buffer
    buffer += "5"
    updateLabel()
def defsix():
    global buffer
    buffer += "6"
    updateLabel()
def defseven():
    global buffer
    buffer += "7"
    updateLabel()
def defeight():
    global buffer
    buffer += "8"
    updateLabel()
def defnine():
    global buffer
    buffer += "9"
    updateLabel()
def defzero():
    global buffer
    buffer += "0"
    updateLabel()
def defplus():
    global buffer,n1,n2,operator
    n1 = buffer
    buffer = ""
    updateLabel()
    operator = "+"
    defrovno()
def defminus():
    global buffer,n1,n2,operator
    n1 = buffer
    buffer = ""
    updateLabel()
    operator = "-"
def defkrat():
    global buffer,n1,n2,operator
    n1 = buffer
    buffer = ""
    updateLabel()
    operator = "*"
def defdeleno():
    global buffer,n1,n2,operator
    n1 = buffer
    buffer = ""
    updateLabel()
    operator = ":"
def defodmoc():
    global buffer,n1,n2,operator
    n1 = buffer
    buffer = ""
    updateLabel()
    operator = "sqr"
def defsin():
    global buffer,n1,n2,operator
    n1 = buffer
    buffer = ""
    updateLabel()
    operator = "sin"
def defrovno():
    global buffer, n1, n2, operator
    n2 = buffer
    match operator:
        case "+":
            buffer = int(n1) + int(n2)
        case "-":
            buffer = int(n1) - int(n2)
        case "*":
            buffer = int(n1) * int(n2)
        case ":":
            buffer = int(n1) / int(n2)
        case "sqr":
            buffer = math.sqrt(int(n1))
        case "sin":
            buffer = math.sin(int(n1))
    updateLabel()
    operator = ""

def defclear():
    global buffer
    buffer = ""
    updateLabel()
#cisla
one = Button(root, text="1", fg="black", bg="white", command=defone, width=4, height=3).grid(row=2, column=0)
two = Button(root, text="2", fg="black", bg="white", command=deftwo, width=4, height=3).grid(row=2, column=1)
three = Button(root, text="3", fg="black", bg="white", command=defthree, width=4, height=3).grid(row=2, column=2)
four = Button(root, text="4", fg="black", bg="white", command=deffour, width=4, height=3).grid(row=3, column=0)
five = Button(root, text="5", fg="black", bg="white", command=deffive, width=4, height=3).grid(row=3, column=1)
six = Button(root, text="6", fg="black", bg="white", command=defsix, width=4, height=3).grid(row=3, column=2)
seven = Button(root, text="7", fg="black", bg="white", command=defseven, width=4, height=3).grid(row=4, column=0)
eight = Button(root, text="8", fg="black", bg="white", command=defeight, width=4, height=3).grid(row=4, column=1)
nine = Button(root, text="9", fg="black", bg="white", command=defnine, width=4, height=3).grid(row=4, column=2)
null = Button(root, text="0", fg="black", bg="white", command=defzero, width=4, height=3).grid(row=5, column=1)
cisla = Label(root, text= buffer, fg="black", bg="gray", width=24)
cisla.grid(row=0, column=0, columnspan=50)
#funkce
rovnase = Button(root,text="=", fg="black", bg="white", command=defrovno, width=4, height=3).grid(row=4, column=5)
soucet = Button(root, text="+", fg="black", bg="white", command=defplus, width=4, height=3).grid(row=2, column=5)
odecet = Button(root, text="-", fg= "black", bg="white", command=defminus, width=4, height=3).grid(row=3, column=5)
Ac = Button(root, text="clear", fg="black", bg="white", command=defclear, width=4, height=3).grid(row=5, column=5)
soucin= Button(root,text="*", fg="black", bg="white", command=defkrat, width=4, height=3).grid(row=2, column=6)
deleno= Button(root, text=":", fg="black", bg="white", command=defdeleno, width=4, height=3).grid(row=3, column=6)
odmoc= Button(root, text="sqr", fg="black", bg="white", command=defodmoc, width=4, height=3).grid(row=4, column=6)
sin= Button(root, text="sin", fg="black", bg="white", command=defsin, width=4, height=3).grid(row=2, column=7)
def updateLabel():
    cisla.config(text=buffer)
root.mainloop()