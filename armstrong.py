import math

def armstrong_check(x):
    s = 0
    for i in x:
        int_x = int(i)
        j = math.pow(int_x, len(x))
        s += j
    if s == int(x):
        return True
    else:
        return False

number = input('Enter a number: ')
if armstrong_check(number):
    print('Entered number is an armstrong number')
else:
    print('Entered number is not an armstrong number')