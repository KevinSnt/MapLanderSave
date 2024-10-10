import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from kevin_luis.views.View import View

"""
    views associated with HomeController. It will be responsible for program's 
    main screen view.
"""
class Homeviews(tk.Tk, View):

    def __init__(self, controller):
        super().__init__()
        self.homeController = controller
        self.createWindow()
        pass
        
    def createWindow(self):
        global window,entry1 ,entries ,countEntries
        countEntries = 0
        window = tk.Tk()
        self.title("Hola como estas")
        window.title("Calculator")
        window.geometry('800x800')

    #label inputs
        entry1 = tk.Entry(window)
        entryOperation1 = tk.Entry(window)
        entry1.grid(row=0, column=0, padx=10, pady=10)
        entryOperation1.grid(row=1, column=0 , padx=10, pady=10)
        btn_add = tk.Button(window, text="+")
        btn_delete = tk.Button(window, text="-")
        btn_add.grid(row=2, column=1, padx=10, pady=10)
        btn_delete.grid(row=3, column=1,padx=10, pady=10)

    #operations buttons
        btnPlus = tk.Button(window, text="+")
        btnPlus.grid(row=0, column=2)
        btnSubstraction = tk.Button(window, text="-")
        btnSubstraction.grid(row=1, column=2)
        btnMultiply = tk.Button(window, text="*")
        btnMultiply.grid(row=2, column=2)
        btnDivide = tk.Button(window, text="÷")
        btnDivide.grid(row=3, column=2)

    #number sistems buttons
        btnBinary = tk.Button(window, text="Binario")
        btnBinary.grid(row=5, column=2 )
        btnOctal = tk.Button(window, text="Octal")
        btnOctal.grid(row=6, column=2)
        btnHex = tk.Button(window, text="Hexadecimal")
        btnHex.grid(row=7, column=2)
        btnDecimal = tk.Button(window, text="Decimal")
        btnDecimal.grid(row=8, column=2)

    #number buttons

        for (num, row, col) in self.homeController.getButtonNumbers():
            btn = tk.Button(window, text=str(num))
            btn.grid(row=row, column=col)

        window.grid_columnconfigure(2, weight=1)

        #window.mainloop()



    #def initComponentWindow():

    #def onClickButton():

    #def onChangeSwitch():

    #def showError():
        #notificar al usuario
        # consola"""
    def constantInput(self):
        global countEntries
        """input1 = tk.Entry(window)
        input1.grid(row=len(window.grid_slaves()) // 2, column=0, padx=10, pady=10)
        """
        #countEntries = 0
        try:
            entriesInput = int(entry1.get())
            if entriesInput == 0:
                messagebox.showinfo("Error", "agregue un numero para AGREGAR LOS INPUT")
            elif countEntries<entriesInput:
                inputnew = tk.Entry(window)
                inputnew.grid(row=len(window.grid_slaves()) // 2, column=0, padx=10, pady=10)
                countEntries += 1
            else:
                messagebox.showinfo("Error", "se alcanzo el maximo de dato seleccionado")
        except Exception as e:
            print(e)
            messagebox.showinfo("Error", "Ingrese un numero valido")
    def deleteInput(self):
        global coutEntries
        entryDelete = entry1.get()
        #if coutEntries >0:

    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
    @Overrite
    """
    def main(self):
        self.mainloop()
        
    """
    @Overrite
    """
    def close(self):
        return
    