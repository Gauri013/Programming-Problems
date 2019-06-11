
def weaves():
    string_one = []
    string_two = []
    string_one = input()
    string_two = input()
    weaved_string = ""
    len_one = len(string_one)
    len_two = len(string_two)
    if (len_one == len_two):
       weaved_string = is_equal(string_one,string_two)
    elif (len_one > len_two):
        weaved_string = first_greater(string_one,string_two)
    else:
        weaved_string = second_greater(string_one,string_two)
    print(weaved_string)

def is_equal(first_string , second_string):
    weaved_string = ""
    for i in range(0,len(first_string)):
        weaved_string += first_string[i] + second_string[i]
    return (weaved_string)

def first_greater(string_one , string_two):
    weaved_string = ""
    for i in range(0,len(string_two)):
        weaved_string += string_one[i] + string_two[i]
    for i in range(len(string_two)+1 , len(string_one)):
        weaved_string += string_two[i]
    return (weaved_string)
                   
def second_greater(string_one , string_two):
    weaved_string = ""
    for i in range(0,len(string_one)):
        weaved_string += string_one[i] + string_two[i]
    for i in range(len(string_one)+1 , len(string_two)):
        weaved_string += string_two[i]
    return (weaved_string)
    
weaves()