num=int(input())
def aliquot():
    x=div(num)
    while(x!=1):
        print(x)
        x=div(x)

    if(x==1):
        print(1)
        print(0)
def div(num):
    temp=num
    nsum=0
    for i in range(1,num):
        if(temp%i==0):
            nsum=nsum+i
    return (nsum)
aliquot()