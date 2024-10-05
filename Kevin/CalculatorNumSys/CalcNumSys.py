#Methods
import sys
from re import match
from string import hexdigits

numbers = []
hexadecimalDigits = '0123456789ABCDEF'
mesageOptionError = "Seleccione una opcion valida dentro del rango de opciones 1, 2, 3, 4, 5"
menuOperation = """Seleccione el numero de la operacion que desea realizar (la operacion se hara en el orden en el que se ingresen los numeros)

         1) Suma
         2) Resta
         3) Multiplicacion
         4) Division
         5) Reiniciar el programa
         6) Terminar 
         """

def opcAmountNumbers():
    global numbers, amount
    while True:
        try:
            amount = int(input("Cuantos numeros desea calcular?: "))
            if amount > 1:
                break
            print("Solo se pueden ingresar valores enteros mayores a 1")
        except ValueError:
            print('No se admiten numeros con punto decimal, letras o cualquier tipo de caracter. Solo valores enteros mayores a 1')
            continue

def validateNumbers(base, number):
    try:
        if number == '':
            raise ValueError("No se puede dejar la casilla vacia")

        if number[0] == '-':
            if len(number) == 1 or number[1] == '0':
                raise ValueError("El numero no puede ser solo un signo negativo o empezar con 0 despues del signo")
            if not number[1:].isdigit() and not validateNumbersByFormat(base, number[1:]):
                raise ValueError(f"El numero debe contener digitos validos despues del signo negativo los cuales son: {baseChars}")

        if number[0] == '0':
            raise ValueError("No puede ingresar solo ceros, ni comenzar con 0")

        if not validateNumbersByFormat(base, number):
            raise ValueError(f"Solo puedes ingresar caracteres validos, los cuales son: '{baseChars}'")

        return True

    except ValueError as e:
        print(e)
        return False

def validateNumbersByFormat(base, number):
    global baseChars
    baseChars = '01' if base == 2 else '01234567' if base == 8 else '0123456789ABCDEFabcdef'

    negativeOrPositive = 1 if number[0] == '-' else 0

    for bit in number[negativeOrPositive:]:
        if bit not in baseChars:
            return False
    return True

def inputNumbers(base):
    for i in range(amount):
        while True:
            number = input(f"Ingrese el numero { i + 1}: ")
            if validateNumbers(base, number):
                numbers.append(str(number))
                break

def binToDecimal(binary):
    isNegative = binary[0] == '-'
    if isNegative:
        binary = binary[1:]

    decimal = 0
    long = len(binary)

    for i in range(long):
        position = binary[long - i - 1]
        if position == '1':
            decimal += 2 ** i

    return -decimal if isNegative else decimal

def octToDecimal(oct):
    isNegative = oct[0] == '-'
    if isNegative:
        oct = oct[1:]

    decimal = 0
    long = len(oct)

    for i in range(long):
        position = oct[long - i - 1]
        decimal +=int(position) * (8 ** i)

    return -decimal if isNegative else decimal

def hexToDecimal(hex):
    isNegative = hex[0] == '-'
    if isNegative:
        hex = hex[1:].upper()
    else:
        hex = hex.upper()

    decimal = 0
    long = len(hex)

    for i in range(long):
        position = hex[long - i - 1]
        if position in hexadecimalDigits:
            decimal += hexadecimalDigits.index(position) * (16 ** i)

    return -decimal if isNegative else decimal

def decimalToBinaryOrOctal(decimal, base):
    if decimal == 0:
        return "0"

    negative = decimal < 0
    if negative:
        decimal = -decimal

    intPart = int(decimal)
    decimalPart = decimal - int(decimal)

    intBinOrOct = ''
    if intPart == 0:
         intBinOrOct = '0'
    else:
        while intPart > 0 and len(intBinOrOct) < 500:
            intBinOrOct = str(intPart % base) + intBinOrOct
            intPart //= base

    decimalBinary = ''
    while decimalPart > 0 and len(decimalBinary) < 200:
        decimalPart *= base
        intPart = int(decimalPart)
        decimalBinary += str(intPart)
        decimalPart -= intPart

    result = intBinOrOct
    if decimalBinary:
        result += '.' + decimalBinary

    return '-' + result if negative else result

def decimalToHex(decimal):
    if decimal == 0:
        return "0"

    negative = decimal < 0
    if negative:
        decimal = -decimal

    intPart = int(decimal)
    decimalPart = decimal - int(decimal)

    intHex = ''
    if intPart == 0:
        intHex = '0'
    else:
        while intPart > 0 and len(intHex) < 500 :
            intHex = hexadecimalDigits[intPart % 16] + intHex
            intPart //= 16

    decimalHex = ''
    while decimalPart > 0 and len(decimalHex) < 200:
        decimalPart *= 16
        intPart = int(decimalPart)
        decimalHex += hexadecimalDigits[intPart]
        decimalPart -= intPart

    result = intHex
    if decimalHex:
        result += '.' + decimalHex

    return '-' + result if negative else result

def addition(numbs):
    result = 0
    for i in numbs:
        result += i

    return result

def subtraction(numbs):
    result = numbs[0]
    for i in numbs[1:]:
        result -= i

    return result

def multiplication(numbs):
    result = numbs[0]
    for i in numbs[1:]:
        result *= i

    return result


def division(numbs):
    result = numbs[0]
    for i in numbs[1:]:
        result /= i

    return result

#Console
while True:
    print("""Que sistema numerico desea utilizar para la operacion?
             (Solo se admitiran numeros sin ningun espacio o tipo de caracter adicional a cada sistema numerico exeptuando un - al inicio para determinar si es un numero negativo) 
    
    1) Binario (Solo numeros 0 y 1)
    2) Octal (Solo numeros 1, 2, 3, 4, 5, 6, 7 )
    3) Hexadecimal (Solo numeros 1, 2, 3, 4, 5, 6, 7, 8, 9 y letras A, B, C, D, E, F)
    """)

    opcNumSys = str(input("Ingrese el numero de la opcion que desea utilizar: "))

    match opcNumSys:
        case "1":
            opcAmountNumbers()
            inputNumbers(2)
            decimalNumbers = [binToDecimal(num) for num in numbers]
            while True:
                print(menuOperation)
                operation = str(input("Ingrese una opcion: "))
                match operation:
                    case "1":
                        sumResult = addition(decimalNumbers)
                        print(decimalToBinaryOrOctal(sumResult, 2))
                    case "2":
                        restResult = subtraction(decimalNumbers)
                        print(decimalToBinaryOrOctal(restResult, 2))
                    case "3":
                        multiResult = multiplication(decimalNumbers)
                        print(decimalToBinaryOrOctal(multiResult, 2))
                    case "4":
                        divisionResult = division(decimalNumbers)
                        print(decimalToBinaryOrOctal(divisionResult, 2))
                    case "5":
                        numbers = []
                        break
                    case "6":
                        sys.exit()
                    case _:
                        print(mesageOptionError)
                        continue

        case "2":
            opcAmountNumbers()
            inputNumbers(8)
            decimalNumbers = [octToDecimal(num) for num in numbers]
            while True:
                print(menuOperation)
                operation = str(input("Ingrese una opcion: "))
                match operation:
                    case "1":
                        sumResult = addition(decimalNumbers)
                        print(decimalToBinaryOrOctal(sumResult, 8))
                    case "2":
                        restResult = subtraction(decimalNumbers)
                        print(decimalToBinaryOrOctal(restResult, 8))
                    case "3":
                        multiResult = multiplication(decimalNumbers)
                        print(decimalToBinaryOrOctal(multiResult, 8))
                    case "4":
                        divisionResult = division(decimalNumbers)
                        print(decimalToBinaryOrOctal(divisionResult, 8))
                    case "5":
                        numbers = []
                        break
                    case "6":
                        sys.exit()
                    case _:
                        print(mesageOptionError)
                        continue

        case "3":
            opcAmountNumbers()
            inputNumbers(16)
            decimalNumbers = [hexToDecimal(num) for num in numbers]
            while True:
                print(menuOperation)
                operation = str(input("Ingrese una opcion: "))
                match operation:
                    case "1":
                        sumResult = addition(decimalNumbers)
                        print(decimalToHex(sumResult))
                    case "2":
                        restResult = subtraction(decimalNumbers)
                        print(decimalToHex(restResult))
                    case "3":
                        multiResult = multiplication(decimalNumbers)
                        print(decimalToHex(multiResult))
                    case "4":
                        divisionResult = division(decimalNumbers)
                        print(decimalToHex(divisionResult))
                    case "5":
                        numbers = []
                        break
                    case "6":
                        sys.exit()
                    case _:
                        print(mesageOptionError)
                        continue

        case _:
            print("Seleccione una opcion valida dentro del rango de opciones 1, 2 o 3 ")
            continue