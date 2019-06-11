def kaprekar_constant(num):
    old = num
    maxNum = max_num(old)
    minNum = min_num(old)
    kap_num = maxNum - minNum
    while(old != kap_num ):
        maxNum = max_num(kap_num)
        minNum = min_num(kap_num)
        old = kap_num
        kap_num = maxNum - minNum
    print(kap_num)

def max_num(num):
    listOfDigits = digits(num)
    length = len(listOfDigits)
    listOfDigits.sort(reverse = True)
    s = 0
    maxNum=0
    for i in range (0,length):
        s = s * 10 + listOfDigits[i]
        maxNum = int(s)
    return maxNum

def min_num(num):
    listOfDigits = digits(num)
    length = len(listOfDigits)
    s = 0
    listOfDigits.sort()
    for i in range (0,length):
        s = s * 10 + listOfDigits[i]
    minNum= s
    return (minNum)

def digits(num):
    listOfDigits = []
    while(num > 0):
        digit = num % 10
        num = int(num // 10)
        listOfDigits.append(digit)
    return(listOfDigits)