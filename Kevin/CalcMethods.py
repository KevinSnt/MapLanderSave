#methods
numbers = []

def numbEnter():
    global numbers
    while True:
        try:
            amount = int(input("Cuantos numeros desea calcular?: "))
            if amount != 0:
                break
            print("Ingrese un valor distinto de 0")
        except ValueError:
            print("Solo se pueden ingresar numeros enteros y y no dejar la casilla vacia ")
            continue

    while True:
        try:
            for i in range(amount):
                number = int(input(f"ingrese el numero {i + 1}: "))
                numbers.append(number)
            break
        except ValueError:
            print("Solo se pueden ingresar numeros enteros y y no dejar la casilla vacia")
            continue


def addition(numbs):
    result = 0
    result = 0
    for i in numbs:
        result += i
    print("El resultado de la suma es: ", result)

def subtraction(numbs):
    result = numbs[0]
    for i in numbs[1:]:
        result -= i
    print("El resultado de la resta es: ", result)

def multiplication(numbs):
    result = numbs[0]
    for i in numbs[1:]:
        result *= i
    print("El resultado de la multiplicacion es: ",result)

def division(numbs):
    result = numbs[0]
    for i in numbs[1:]:
        result /= i
        print("El resultado de la division es: ",result)


#####################
numbEnter()
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
            addition(numbers)
        case "2":
            subtraction(numbers)
        case "3":
            multiplication(numbers)
        case "4":
            division(numbers)
        case "5":
            numbEnter()
        case "6":
            break