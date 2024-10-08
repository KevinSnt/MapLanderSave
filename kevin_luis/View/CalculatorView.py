import tkinter
import tkinter as tk
from tkinter import *
from math import *

def createWindow():
    window = tk.Tk()
    window.title("Calculator")
    window.geometry('800x800')

    entry1 = tk.Entry(window)
    entry1.grid(row=0, column=0, padx=10, pady=10)
    btn_suma = tk.Button(window, text="+")
    btn_suma.grid(row=0, column=1)

    btn_suma = tk.Button(window, text="+")
    btn_suma.grid(row=0, column=2)
    btn_resta = tk.Button(window, text="-")
    btn_resta.grid(row=1, column=2)
    btn_multiplicacion = tk.Button(window, text="*")
    btn_multiplicacion.grid(row=2, column=2)
    btn_division = tk.Button(window, text="÷")
    btn_division.grid(row=3, column=2)

    ButtonDigit1 = tk.Button(window, text="1")
    ButtonDigit1.grid(row=0, column=3)
    ButtonDigit2 = tk.Button(window, text="2")
    ButtonDigit2.grid(row=0, column=4)
    ButtonDigit3 = tk.Button(window, text="3")
    ButtonDigit3.grid(row=0, column=5)
    ButtonDigit4 = tk.Button(window, text="4")
    ButtonDigit4.grid(row=1, column=3)
    ButtonDigit5 = tk.Button(window, text="5")
    ButtonDigit5.grid(row=1, column=4)
    ButtonDigit6 = tk.Button(window, text="6")
    ButtonDigit6.grid(row=1, column=5)
    ButtonDigit7 = tk.Button(window, text="7")
    ButtonDigit7.grid(row=2, column=3)
    ButtonDigit8 = tk.Button(window, text="8")
    ButtonDigit8.grid(row=2, column=4)
    ButtonDigit9 = tk.Button(window, text="9")
    ButtonDigit9.grid(row=2, column=5)
    ButtonDigit0 = tk.Button(window, text="0")
    ButtonDigit0.grid(row=3, column=3)
    ButtonPower = tk.Button(window, text="^")
    ButtonPower.grid(row=3, column=4)
    ButtonFraction = tk.Button(window, text="/")
    ButtonFraction.grid(row=3, column=5)
    ButtonResult = tk.Button(window, text="=")
    ButtonResult.grid(row=4, column=3)

    window.grid_columnconfigure(2, weight=1)

    window.mainloop()

#def initComponentWindow():

#def onClickButton():

#def onChangeSwitch():

#def showError():
    #notificar al usuario
    # consola"""

if __name__ == '__main__':
    createWindow()