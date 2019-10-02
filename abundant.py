# Program to check abundant number

def abundant_check(number):
    # number is int type
    divisor_list = []
    for i in range(1, number):
        if number%i == 0:
            divisor_list.append(i)
    if sum(divisor_list) > number:
        return True
    else:
        return False

number = int(input('Enter any number: '))
if abundant_check(number):
    print(str(number) + ' is an abundant number')
else:
    print(str(number) + ' is not an abundant number')

