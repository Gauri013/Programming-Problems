def triple():
    a = 0
    b = 0
    c = 0
    lst = []
    triple_lst = []
    count = 0
    while (count != 11):
        for i in range (0 , 10000):
            for j in range ( i, 10000):
                for k in range(j, 10000):
                    if (i**3 + j**3 == c**2):
                        lst.append(i)
                        lst.append(j)
                        lst.append(k)
                    triple_lst.append(lst[count])
                    count += 1
    return (triple_lst)

def ten_triple():
    triple_list = triple()
    for i in range (0,10):
        print (triple_list[i])

ten_triple()
