#converting the binary strings into decimal
def binaryToDecimal(decimalNumber):
    firstInput=0
    firstNumber=1
    for k in reversed(decimalNumber):
                firstInput+=firstNumber*int(k)
                firstNumber=firstNumber*2
    return firstInput
    
