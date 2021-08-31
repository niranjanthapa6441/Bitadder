#imorting the necessary modules
import gate as gt
import decimalToBinary as dtb
import binaryToDecimal as btd
import checkingTheSizeofTheList as ctsol
def adder():
    #creates and controls a while loop to let user input multiple values
    multipleTimes=False
    while multipleTimes==False:
        #checks the typeError in program
        try:
            #holds the value returned by the respective function from decimalToBinary module 
            a=ctsol.checkinTheSizeOfList(dtb.firstNumber())
            b=ctsol.checkinTheSizeOfList(dtb.firstNumber())
            # changing list into strings
            firstString=''.join([str(z) for z in a])
            secondString=''.join([str(s) for s in b])
            firstInput=btd.binaryToDecimal(a)
            secondInput=btd.binaryToDecimal(b)
            print('First Input is: {}({})'.format(firstString,firstInput))
            print('Second Input is: {}({})'.format(secondString,secondInput))
            #checks the size of the list and appends necessary values in the required list 
            carryOver=0
            sumValues=[]
            result=''
            """iterating through the list and sending the values to the function
            in gates module forming a byte adder"""
            for i in range(len(a)-1,-1,-1):
                firstSumValue=gt.xorGate(a[i],b[i])
                sumValue=gt.xorGate(firstSumValue,carryOver)

                firstCarryOver=gt.andGate(a[i],b[i])
                secondCarryOver=gt.andGate(firstSumValue,carryOver)  
                carryOver=gt.orGate(firstCarryOver,secondCarryOver)
                sumValues.append(sumValue)
            if carryOver==1:
                result+=str(carryOver)
            #reversing the list and concatenating the value in strings 
            for j in reversed(sumValues):
                result+=str(j)  
            value=btd.binaryToDecimal(result)
            print('sum is: {}({})'.format(result,value))
            #creatnig a while loop to control the multiple input from the user
            checked=False
            while checked==False:
                n=input("Do you want to continue Y/N: ")
                if n.lower()== 'y':
                    multipleTimes=False
                    checked=True
                elif n.lower()== 'n':
                    multipleTimes=True
                    print("Thank You")
                    checked=True
                else:
                    print('invalid')
                    checked=False
        #handles the error in program
        except TypeError:
            print("please input the integer value")
        
adder()
