try:
    variable1 = float(input("ingresa el primer dato"))
except ValueError:
    print("solo numeros")
variable2 = float(input("ingresa el segundo dato"))
print(variable1 + variable2)
print(variable1 - variable2)
print(variable1 * variable2)
print(variable1 / variable2)