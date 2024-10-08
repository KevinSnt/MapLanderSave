from tkinter import *
from math import *
import tkinter as tk
from tkinter import ttk,messagebox


def createWindow():
    window = tk.Tk()
    data = ttk.Entry(window)
    bottomAddNum = ttk.Button(text="+",width=10)
    #title
    window.title("Calculator")
    window.geometry('800x800')

    #position
    bottomAddNum.place(x = 100, y= 100)
    window.mainloop()
#def initComponentWindow(window):
   



def onClickButton():


#def onChangeSwitch():

#def showError():
    #notificar al usuario
    # consola"""

if __name__ == '__main__':
    createWindow()