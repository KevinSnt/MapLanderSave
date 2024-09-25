#methods
numero1 = 0
numero2 = 0
def introNums():
    while True:
        try:
            numero1 = int(input("ingrese el primer numero: "))
            break
        except ValueError:
            print("Solo se pueden ingresar numeros enteros y y no dejar la casilla vacia")
            continue

    while True:
        try:
            numero2 = int(input("ingrese el segundo numero: "))
            break
        except ValueError:
            print("Solo se pueden ingresar numeros enteros y y no dejar la casilla vacia")
            continue

def suma(num1, num2):
    return("El resultado de la suma es: ",num1 + num2)

def resta(num1, num2):
    print("El resultado de la resta es: ",num1 - num2)

def multiplicacion(num1, num2):
    print("El resultado de la multiplicacion es: ",num1 * num2)

def division(num1, num2):
    if num2==0:
        print("no se puede dividir entre 0")
    else:
        print("El resultado de la division es: ",num1 / num2)


#####################
introNums()
while True:
    print("""
         seleccione el numero de la operacion que desea realizar

         1) Suma
         2) Resta
         3) Multiplicacion
         4) Division
         5) Cambiar numeros
         6) Terminar 
         """)
    operacion = str(input("ingrese una opcion: "))

    match operacion:
        case "1":
            suma(numero1, numero2)
        case "2":
            resta(numero1, numero2)
        case "3":
            multiplicacion(numero1, numero2)
        case "4":
            division(numero1, numero2)
        case "5":
            introNums()
        case "6":
            break


