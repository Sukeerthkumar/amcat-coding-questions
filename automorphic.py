# Program to check if a given number is automorphic or not

def automorphic_check(number):
    squared = str(int(number)**2)
    r_squared = squared[::-1]
    r_check = []
    i = len(number)
    for x in r_squared:
        if i == 0:
            break
        r_check.append(x)
        i -= 1
    check_number = ''.join(r_check[::-1])
    if check_number == number:
        return True
    else:
        return False

number = input('Enter any number: ')
if automorphic_check(number):
    print(number + ' is an automorphic number')
else:
    print(number + ' is not an automorphic number')