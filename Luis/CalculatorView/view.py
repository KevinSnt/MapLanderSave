import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import INSERT


def plus():

    try:
        if verifiNumbers() == True:
            if signeCondition() == True:
                numbers = [float(num) for num in data.get().split(",")]
                result = numbers[0]
                for num in numbers[1:]:
                    result += num
                messageResult(result)
            else:
                print("el usuario ingreso signo")
        else:
            errorConsole()

            #numbersCheck = data.get().split(",")
        #for condition in numbersCheck:
        # if  "e+" in condition or "E+" in condition:
        #     messageError()
    except ValueError:
        print("Registro de errpr")



def subtract():
    try:
        if verifiNumbers() == True:
            numbers = [float(num) for num in data.get().split(",")]
            if signeCondition() == True:
                if len(numbers) > 2:
                    messageCondition()
                else:
                    result = numbers[0]
                    for num in numbers[1:]:
                        result -= num
                    messageResult(result)
            else:
                print("No se permiten signos en esta calculadora")
        else:
            errorConsole()
    except ValueError:
       messageError()


def multiply():
    try:
        if verifiNumbers() == True:
            numbers = [float(num) for num in data.get().split(",")]

            result = numbers[0]
            for num in numbers[1:]:
                result *= num
            messageResult(result)
    except ValueError:
        messageError()


def divide():
    try:
        if verifiNumbers() == True:
            numbers = [float(num) for num in data.get().split(",")]
            if len(numbers)>=3:
                messageCondition()
            else:
                if numbers[1] == 0:
                    messageErrorDivide()
                else:
                    result = numbers[0]
                    for num in numbers[1:]:
                        result /= num
                    messageResult(result)

    except ValueError:
        messageError()
        print(ValueError)


#Show Message Error
def messageError ():
    messagebox.showinfo('Error', f'Ingresa un numero valido, dividido por "," o no ingrese numeros con notacion "2+e22"')


def messageResult(result):
    messagebox.showinfo('Resultado', f'El resultado es:{result}')


def messageErrorDivide():
    messagebox.showinfo('Error', f'No puedes dividir entre 0')


def messageCondition():
    messagebox.showinfo('Error', f'para esta operacion solo se permite dos numeros')


def errorConsole():
    print("Error 404")

#Verifi numbers
def verifiNumbers():
    numbersCheck = data.get().split(",")
    for condition in numbersCheck:
        if "e+" in condition or "E+" in condition or "e" in condition or "E" in condition:
            messageError()
            return False
    return True
def signeCondition():
    numbersCheck = data.get().split(",")
    for condition in numbersCheck:
        if "-" in condition or "+"  in condition or "*" in condition or "/" in condition:
            messagebox.showinfo('Error', "no se permiten signos en esta operacion")
            return False
    return True

def instructions():
    messagebox.showinfo("Informacion","Bienvenido a la calculadora basica, solo se permite meter numeros sin signos separado por comas ejemplo (2,2,2)"
                        +"al igual en la resta y division solo son entre dos numeros ejemplo (2,2)")
def view ():
    #declarando
    global data
    root = tk.Tk()
    #root.insert(INSERT,"Por favor Ingrese los datos que desea calcular, divivido por comas por ejemplo 2,3,4,1,2")
    data=ttk.Entry(root)
    bottomSum = ttk.Button(text='Suma',command=plus,width=10)
    bottomSubstract = ttk.Button(text='Resta',command=subtract,width=10)
    bottomMultiply = ttk.Button(text='Multiplicacion',command=multiply,width=10)
    bottomDivide = ttk.Button(text='Divison',command=divide,width=10)


    #title
    root.title("Calculator")
    text = "Ingresa los datos"
    instruction = tk.Label(root, text=text)
    root.geometry('300x400')

    #Position
    data.place(x=75, y=50)
    bottomSum.place(x=100,y=120)
    bottomSubstract.place(x=100, y=150)
    bottomMultiply.place(x=100, y=180)
    bottomDivide.place(x=100, y=210)

    root.mainloop()

if __name__ == '__main__':
    instructions()
    view()

