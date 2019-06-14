from functools import reduce
def sumSquareDiff():
    lst = [i for i in range(1, 101)]
    sq_lst = [i*i for i in range(1, 101)]
    sumOfNum = reduce(computeSum , lst)
    sumOfSqnum = reduce(computeSum , sq_lst)
    sumOfNum *= sumOfNum
    return (sumOfNum - sumOfSqnum)

def computeSum( v1 , v2):
    return v1 + v2

print(sumSquareDiff())