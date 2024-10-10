#poner los textos, errores
plusCase = "plus"
subtractCase = "subtract"
multiplyCase = "multiply"
divideCase = "divide"
binaryCase = "binary"
octalCase = "octal"
hexaCase= "hexa"
decimalCase = "decimal"
typeNumbersMAp = {
    'decimal': [('0', 0, 3), ('1', 0, 4), ('2', 0, 5),
                ('3', 1, 3), ('4', 1, 4), ('5', 1, 5),
                ('6', 2, 3), ('7', 2, 4), ('8', 2, 5),
                ('9', 3, 3)],
    'binary': [('0', 0, 3), ('1', 0, 4)],
    'octal': [('0', 0, 3), ('1', 0, 4), ('2', 0, 5),
              ('3', 1, 3), ('4', 1, 4), ('5', 1, 5),
              ('6', 2, 3), ('7', 2, 4)],
    'hexadecimal': [('0', 0, 3), ('1', 0, 4), ('2', 0, 5),
                    ('3', 1, 3), ('4', 1, 4), ('5', 1, 5),
                    ('6', 2, 3), ('7', 2, 4), ('8', 2, 5),
                    ('9', 3, 3), ('A', 3, 4), ('B', 3, 5),
                    ('C', 4, 3), ('D', 4, 4), ('E', 4, 5),
                    ('F', 5, 3)]
}