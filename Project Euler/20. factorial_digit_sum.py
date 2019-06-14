from functools import reduce

def multiply( v1 , v2):
    return v1*v2

def factorial(num):
    lst = [ i for i in range(num ,1 , -1)]
    return reduce(multiply , lst)

def Computesum():
    num = str(factorial(100))
    digits =[int(i) for i in num]
    return sum(digits)

print(Computesum())
