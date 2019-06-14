def palin(num):
    t = num
    if (t == num[::-1]):
        return True
    else:
        return False
def compute_highest_palin():
    for i in range (999999 , 100000 , -1):
        if( palin(list(str(i)))) and printMul(i) != None:
            return printMul(i)

def printMul(num):
    for i in range (999,100 , -1):
        for j in range (999, 100 , -1):
            if(i * j == num):
                return [i ,j]
            
lst = compute_highest_palin()
print (lst[0] , "*", lst[1], "=", lst[0]*lst[1])

