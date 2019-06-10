str_print = "#"
space = " "
str_print2 = "-"
def pattern(num):
    num -= 1
    j = 1
    i = 0
    print(str_print.center(80))
    while(i < num):
        first_space = spaces(num,i)
        char_displayed = charToDisplay(j)
        last_space = spaces(num,i)
        print((first_space + char_displayed+last_space).center(80))
        j += 2
        i += 1
        
def spaces(num,i):
    return (space * (num - 1 - i))

def charToDisplay(j):
    new_str_print = str_print + str_print2 * j+ str_print
    return(new_str_print)

pattern(4)

