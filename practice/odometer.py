from itertools import combinations
def all_value(key):
    odometer = []
    list_of_digits = [1,2,3,4,5,6,7,8,9]
    for i in list(combinations(list_of_digits , key)):
        value = 0
        if ((i[0] < i[1]) and (i[1] < i[2])):
            for j in i:
                value = value*10 + j
            odometer.append(value)
    return(odometer)

def previous_value(readings , current_value, n):
    index = readings.index(current_value)
    previous_list = []
    for i in range (0 , n):
        previous_list.append(readings[index - 1])
        index -= 1   
    return previous_list

def next_value(readings , current_value, n):
    index = readings.index(current_value)
    nextVal_list = []
    for i in range (0 , n):
        nextVal_list.append(readings[index + 1])
        index += 1   
    return nextVal_list

def distanceBetweenValues(val_one , val_two, readings):
    distance = readings.index(val_two) - readings.index(val_one) - 1
    return distance

current_value = input()
second_value = input()
n = int(input())
key = len(current_value)
readings = all_value(key)
print("previous value :" ,previous_value(readings , int(current_value) , n))
print("next value :" ,next_value(readings , int(current_value) , n))
print("distance between" , current_value ,"and", second_value ,"is", distanceBetweenValues(int(current_value),int(second_value) , readings))
    
