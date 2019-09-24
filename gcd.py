# Program to find GCD | HCF of two numbers - Euclidean algorithm

def gcd(x,y):
    if x == 0:
        return y
    return gcd(y%x, x)

l = [int(x) for x in input('Enter two numbers: ').split()]
gcd = gcd(l[0], l[1])
print('GCD of ' + str(l[0]) + ' and ' + str(l[1]) + ' is: ' + str(gcd))
