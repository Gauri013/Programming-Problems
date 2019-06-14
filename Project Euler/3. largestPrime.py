def compute_highest_factor(num):
    for i in range(int(num/2),1, -1):
        if ((num % i == 0) and (isprime(i))):
            return i 

def isprime(n):
    count = 0
    for i in range ( 2 , int(n/2)):
        if (n % i == 0):
            count += 1
    if(count == 0):
        return True
    else:
        return False
        

def print_factor(num):
    factor = compute_highest_factor(num)
    print ("highest factor is" , factor)

num = int(input())
print_factor(num)