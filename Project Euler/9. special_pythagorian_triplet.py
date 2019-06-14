from itertools import combinations
from math import sqrt
def square():
  return [i*i for i in range (3,500)]

def PythagorianTriplet():
    sq_lst = square()
    triplet_lst = []
    return [(i[0] ,i[1] ,i[2]) for i in combinations(sq_lst , 3) if (i[0] + i[1] == i[2])]
        
def specialTriplet():
    return [(sqrt(i[0]) , sqrt(i[1]) ,sqrt(i[2])) for i in PythagorianTriplet() if (sqrt(i[0]) + sqrt(i[1]) +sqrt(i[2]) == 1000)]

print(specialTriplet())
    