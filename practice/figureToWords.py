def figureToWords(num: int):

    dict_0_19 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Tweleve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    dict_20_90 = {20 : 'Twenty',30 : 'Thirty', 40 : 'Forty',50 : 'Fifty',60 : 'Sixty',70 : 'Seventy',80 : 'Eighty',90 : 'Ninety'}
    dict_other = {100 :'Hundred', 1000 : 'Thousand'}

 

    if ( num % 10 == 0):
        print(dict_20_90[n])
 
    else :
        digits = list_digits(num)
        temp=0
        word = []
        current = []
        for i in range(len(digits)-1,-1,-1):
            current.append(digits[i] * (10 ** (len(digits)-i-1)))
 
        current.append(0)
        temp = current[0]+current[1]
        if( temp < 20) :
            word.append(dict_0_19[temp])
        else :
            word.append(dict_0_19[current[0]])
            word.append(dict_20_90[current[1]])
        for i in range(2,len(digits)):
            temp= current[i]
            t = 10 ** i
            word.append(dict_other[t])
            word.append(dict_0_19[(temp//t)])
 
        word.reverse()
        s = ""
        for i in range (0,len(word)):
            s = s +" "+ word[i]
        print(s)
 


def list_digits(num):
    digit=[]
    while num != 0 :
        digit.append(num % 10)
        num = num // 10
    digit.reverse()
    return digit
 
import sys
num = int(input())
figureToWords(num)