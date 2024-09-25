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

     operacion = str(input(" "))

     match operacion:
            case "1":
                print("El resultado de la suma es: ",numero1 + numero2)

            case "2":
                 print("El resultado de la resta es: ",numero1 - numero2)

            case "3":
                print("El resultado de la multiplicacion es: ",numero1 * numero2)

            case "4":
                if numero2 == 0:
                     print("no se puede dividir entre 0")
                else:
                    print("El resultado de la division es: ",numero1 / numero2)
            case "5":
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
            case "6":
                break
            case _:
                print("Seleccione una opcion valida dentro del rango de opciones")
                continue

