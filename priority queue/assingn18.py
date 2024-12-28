def printN(n):
    if n > 0:
        printN(n-1)
        print(n,end=' ')
def printNrevers(n):
    if n>0:
        print(n,end=' ')
        printNrevers(n-1)
def printNOdd(n):
    if n > 0:
        printNOdd(n-1)
        print(2*n-1,end=' ')  
printNOdd(10)

def printNEven(n):
    if n > 0:
        printNEven(n-1)
        print(2*n,end=' ') 
printNEven(10)