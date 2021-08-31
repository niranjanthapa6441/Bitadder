#declaring a function to take input integer and convert it into binary string
def firstNumber():
    entered=False
    """creating a while loop to check
    wthether the input is valid or not,
    if not then letting users to re-input the valid value"""
    while entered==False:
        #checking the valueError
        try:
            l=[]
            n=int(input("Enter the number "))
            if n>255 or n<0:
                print("Invalid input!!please input the integers from 0-255")
                entered=False
            else:
                entered=True
        #handling the ValueError
        except ValueError:
            print("Please enter integer value only")
    #creating a while loop and appending the value of input in the list until the dividend is 0
    while n>0:
        if n%2==0:
            l.append(0)
        else:
            l.append(1)
        n=int(n/2)
    l1=[]
    #iterating through the reverse index of list
    for i in reversed(l):
        l1.append(i)
    return l1

