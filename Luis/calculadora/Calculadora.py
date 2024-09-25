from select import select
while True:
    try:
        data1 = float(input("digite el valor de la suma:"))
    except ValueError:
        print("solo numeros")
        continue
    try:
        data2 = int(input("digite el valor de la segunda variable:"))
    except ValueError:
        print("solo numeros")
        continue
    print("Bienvenido al Calculadora de Python:\n"+
          "1:suma\n"+
          "2:restar\n"+
          "3:multiplicacion\n"+
          "4:dividir\n"+
          "5:salir\n")



    option = (input("que deseas hacer:\n"))
    match option:
        case "1":
            print("La suma es:\n")
            print(data1+data2)

        case "2":
            print("resta:\n")
            print(data1 - data2)

        case "3":
            print("La multiplicacion es:")
            print(data1 * data2)

        case "4":
            print("La division es:\n")
            print(data1 / data2)

        case "5":
            print("saliendo")
            break
        case _:
            print("seleccione un dato que exista en las opciones")
            continue
