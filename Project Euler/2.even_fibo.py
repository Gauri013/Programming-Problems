def fibo(start , end , count ,cal_sum):
    output = ""
    fib_no = start + end
    start = end
    end = fib_no
    if (fib_no % 2 == 0):
        cal_sum += fib_no
    count -= 1
    print (fib_no)
    if count != 0:
        fibo(start , end , count , cal_sum)
    else :
         output = even_sum(cal_sum)
         print (output)
    

def even_sum(cal_sum):
    return "the sum is :" ,cal_sum

print(1)
print(2)
fibo(1,2 ,30 , 2)