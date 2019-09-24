# Program to check if given number is prime or not
import math

def prime_check(x):
    flag = 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            flag = 1
            break
    if flag == 1:
        print(str(x) + ' is not a prime number')
    else:
        print(str(x) + ' is a prime number')

x = int(input('Enter any number: '))
prime_check(x)