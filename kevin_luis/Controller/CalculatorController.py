from ..utils import constans,utils
#Luis
def calculatePlus():
def calculateSubstract():
def calculateMultiply():
def calculateDivide():
def calculatorOperation(typeOperation):
    match (typeOperation):
        case constans.plusCase:
            calculatePlus()
            break
        case constans.substractCase:
            calculateSubstract()
            break
        case constans.multiplyCase:
            calculateMultiply()
            break
        case constans.divideCase:
            calculateDivide()
            break
        case "_":
            break




#kevin
def validateSystemNumbers(typeSystemNumber,number):
    match (typeSystemNumber):
        case constans.binaryCase:
            utils.validateFormat(number, 'binario')
            break
        case constans.octalCase:
            utils.validateFormat(number, 'octal')
            break
        case constans.hexadecimalCase:
            utils.validateFormat(number, 'hexadecial')
            break
        case constans.decimalCase:
            utils.validateFormat(number,'decimal')
            break
        case "_":
            break

def numberSystemConvertion(number,typeSystemNumber):
    match (typeSystemNumber):
        case constans.binaryCase:
            binaryToDecimal(number)
            break
        case constans.octalCase:
            octalToDecimal(number)
            break
        case constans.hexadecimalCase:
            hexToDecimal(number)
            break
        case constans.decimalCase:
            decimalToConvert(number)
            break



def binaryToDecimal():



def octalToDecimal():



def hexToDecimal():



def decimalToConvert():



