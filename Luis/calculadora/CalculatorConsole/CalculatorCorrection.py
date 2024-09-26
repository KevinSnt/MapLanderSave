from select import select
def sum(dataNumbers):
    result = dataNumbers[0]
    for num in dataNumbers[1:]:
        result += num
    return result
def subtract(dataNumbers):
    result = dataNumbers[0]
    for num in dataNumbers[1:]:
        result -= num
    return result
def multiply(dataNumbers):
    result = dataNumbers
    for num in dataNumbers:
        result *= num
    return result
def divide(dataNumbers):
    result = dataNumbers[0]
    for num in dataNumbers:
        result /= num
    return result

def data():
    dataNumbers = []
    while True:
        try:
            num = float(input("Ingrese la cantidad de numeros que deseas poner, si deseas salir coloque cualquier tecla que no sea numero:\n "))
            dataNumbers.append(num)
        except ValueError:
            print("saliendo")
            break
    return dataNumbers



def options(dataNumbers):
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
                print(sum(dataNumbers))

            case "2":
                print("resta:\n")  # -2 y metros cuadrados
                print(subtract(dataNumbers))

            case "3":
                print("La multiplicacion es:")  #
                print(subtract(dataNumbers))

            case "4":
                print("La division es:\n")
                print(divide(dataNumbers))

            case "5":
                data()
            case "6":
                print("saliendo del programa :)\n")
                break
            case _:
                print("seleccione un dato que exista en las opciones")
                continue



if __name__ == "__main__":
    dataNumbers = data()
    options(dataNumbers)

