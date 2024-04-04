from tkinter import *
nwin= Tk()

name= Label(nwin, text= "Name").grid(row=0, column=0)
entry1= Entry(nwin).grid(row= 0, column= 1)

password= Label(nwin, text= "Password").grid(row= 1, column= 0)
entry2= Entry(nwin).grid(row= 1, column= 1)
