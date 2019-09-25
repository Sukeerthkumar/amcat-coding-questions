# Program to check if number is a strong number or not

def factorial(x):
    if x < 1:
        return 1
    else:
        return x*factorial(x-1)

def strong_check(x):
    s = 0
    for i in x:
        int_x = int(i)
        s += factorial(int_x)
    if s == int(x):
        return True
    else:
        return False

number = input('Enter any number: ')
if strong_check(number):
    print('Entered number is a strong number')
else:
    print('Entered number is not a strong number')
