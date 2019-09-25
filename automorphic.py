# Program to find if number is automorphic or not

def automorphic_check(x):
    squared = str(int(x) ** 2)
    diff = len(squared) - len(x)
    squared = squared[diff:]
    if squared == x:
        return True
    else:
        return False

number = input('Enter any number: ')
if automorphic_check(number):
    print('Entered number is an automorphic number')
else:
    print('Entered number is not an automorphic number')

