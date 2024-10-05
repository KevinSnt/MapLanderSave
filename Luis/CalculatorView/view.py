import tkinter as tk
from logging import exception
from tkinter import ttk, messagebox,Label
from decimal import Decimal


def plus():
    if conditionSigne() == True:
        try:
            result = getNumbers()[0]
            for num in getNumbers()[1:]:
                result += num
            messageResult(result)
        except Exception as e:
            messageError()
            print(e)
    else:
        print("hay mas de un signo")


def subtract():
    try:
        result = getNumbers()[0]
        for num in getNumbers()[1:]:
            result -= num
        messageResult(result)

    except Exception as e:
       messageError()
       print(e)



def multiply():
    try:
            result = getNumbers()[0]
            for num in getNumbers()[1:]:
                result *= num
            messageResult(result)

    except Exception as e:
        messageError()
        print(e)


def divide():
    try:
            if len(getNumbers())>=3 or len(getNumbers())==1:
                messageCondition()
            else:
                if getNumbers()[1] == 0:
                    messageErrorDivide()
                else:
                    result = getNumbers()[0]
                    for num in getNumbers()[1:]:
                        result /= num
                    messageResult(result)

    except Exception as e:
        messageError()
        print(e)


#Show Message Error
def messageError ():
    messagebox.showinfo('Error', f'Ingresa un numero valido, dividido por comas ","')


def messageResult(result):
        showResult = str(result)
        messagebox.showinfo('Resultado', f'El resultado es:{showResult[:10]}')


def messageErrorDivide():
    messagebox.showinfo('Error', f'No puedes dividir entre 0')


def messageCondition():
    messagebox.showinfo('Error', f'para la division, solo se permite dividir en dos numeros')


def errorConsole():
    print("Error 404")

def conditionSigneView(signeError):
    messagebox.showinfo('Error', f'no puedes agregar mas de un signo : {signeError}')

#Verifi numbers
"""def signeCondition(validate_numbers):
    for condition in validate_numbers:
        if "-" in condition or "+"  in condition or "*" in condition or "/" in condition:
            messagebox.showinfo('Error', "no se permiten signos en esta operacion")
            return False
    return True"""


"""def instructions():
    messagebox.showinfo("Informacion","Bienvenido a la calculadora basica, solo se permite meter numeros sin signos separado por comas ejemplo (2,2,2)"
                        +"al igual en la resta y division solo son entre dos numeros ejemplo (2,2)")"""


def getNumbers():
    try:
        numbers = [float(num) for num in validateSigne()]
        return numbers
    except Exception as e:
        print(e)
       # messagebox.showinfo("error","Error esta en la longitud que ingresaste")


def addInput():#Generar una vista al momento de llamar al metodo
        #new input
    newInput = ttk.Entry(root)
        #position
    newInput.place(x=100, y=100)


def conditionSigne():
    validate = [data.get()]  # Assuming data.get() returns a string
    for value in validate:
        if value.count('^') > 1:
            messagebox.showinfo('Error', "No puedes agregar más de un signo (^) ")
            return False
        if value.count('/') > 1:
            messagebox.showinfo('Error', "No puedes agregar más de un signo (/) ")
            return False
    return True


def validateSigne ():
    try:
        validateNumbers = data.get().split(",")
        for i in range(len(validateNumbers)):
            condition = validateNumbers[i]
            if "/" in condition:
                num1, num2 = condition.split("/")
                result = float(num1) / float(num2)
                validateNumbers[i] = result
            if "^" in condition:
                num1, num2 = condition.split("^")
                result = float(num1) ** float(num2)
                validateNumbers[i] = result

        return validateNumbers
    except Exception as e:
        print(e)
        messagebox.showinfo("error", "El resultado es muy grande para ser procesado.")


def view ():
    #declarando
    global data, root
    root = tk.Tk()
    #instruction = ttk.Label(text='Ingresa los datos separados por comas:(2,2)')
    data=ttk.Entry(root)
    bottomSum = ttk.Button(text='Suma',command=plus,width=10)
    bottomSubstract = ttk.Button(text='Resta',command=subtract,width=10)
    bottomMultiply = ttk.Button(text='Multiplicacion',command=multiply,width=10)
    bottomDivide = ttk.Button(text='Divison',command=divide,width=10)


    #title
    root.title("Calculadora")
    text = ("Ingrese los datos que desee sumar restar o multiplicar separado por comas (2,5,2)\n"
            +"en division solamente se aceptan 2 numeros divididos por comas ( , ) ")
    instruction = tk.Label(root, text=text)
    root.geometry('500x400')

    #Position

    instruction.place(x = 27,y = 25)
    data.place(x=175, y=80)
    bottomSum.place(x=195,y=120)
    bottomSubstract.place(x=195, y=150)
    bottomMultiply.place(x=195, y=180)
    bottomDivide.place(x=195, y=210)

    root.mainloop()

if __name__ == '__main__':
    #instructions()
    view()

