from select import select
def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def data():
    global data1,data2
    while True:
        try:
            data1 = float(input("digite el primer valor:"))
        except ValueError:
            print("solo numeros")
            continue
        try:
            data2 = float(input("digite el valor de la segunda variable:"))
            break
        except ValueError:
            print("solo numeros")
            continue



def options():
    while True:
        print("Bienvenido al Calculadora de Python\n" +
              "1:suma\n" +
              "2:restar\n" +
              "3:multiplicacion\n" +
              "4:dividir\n" +
              "5:seleccionar otros numeros:\n"  
              "6:salir\n")
        option = (input("que deseas hacer:\n"))
        match option:
            case "1":
                print("La suma es:\n")  # 1 y m
                print(sum(data1, data2))

            case "2":
                print("resta:\n")  # -2 y metros cuadrados
                print(subtract(data1, data2))

            case "3":
                print("La multiplicacion es:")  #
                print(subtract(data1, data2))

            case "4":
                print("La division es:\n")
                print(divide(data1, data2))

            case "5":
                data()
            case "6":
                print("saliendo del programa :)\n")
                break
            case _:
                print("seleccione un dato que exista en las opciones")
                continue



if __name__ == "__main__":
    data()
    options()

