# Program to check abundant number

def abundant_check(number):
    # number is int type
    divisor_list = []
    for i in range(1, number):
        if number%i == 0:
            divisor_list.append(i)
    print(divisor_list)
    if sum(divisor_list) > number:
        print(str(True))
    else:
        print(str(False))

abundant_check(12)