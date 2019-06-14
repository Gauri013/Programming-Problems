from functools import reduce
from math import gcd

def lcm(v1, v2):
    return v1*v2 // gcd(v1,v2)

def compute_answer():
    lst = [i for i in range(1,21)] 
    return reduce(lcm , lst)

print(compute_answer())
