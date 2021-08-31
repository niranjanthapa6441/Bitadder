#defining the function of gates
def xorGate(x,y):
    if (x==0 and y==0) or (x==1 and y==1):
        return 0
    else:
        return 1

def orGate(x,y):
    if x==0 and y==0:
        return 0
    else :
        return 1

def andGate(x,y):
    if x==1 and y==1:
        return 1
    else:
        return 0

    
