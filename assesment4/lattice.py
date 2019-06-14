import math
def termins(lattice_point : tuple , lst : list) -> tuple:
    x = 0
    y = 0
    X = 0.0
    Y = 0.0
    dict_compass = {"N" : 360 , "S" : 180 , "NE": 45 , "SE": 135, "E":90, "NW": 315 , "W":270 , "SW":225}
    x = dict_compass[lst[0[1:]]]
    X = lattice_point[0] + ( lst[0[:1]]*math.sin(x))
    x = dict_compass[lst[1[1:]]]
    Y = lattice_point[1] + (lst[1[:1]]*math.cos(x))
    tup = (X, Y)
    return tup
tup = tuple(input())
lst = list(input())
answer =termins( tup , lst)
print(answer)
