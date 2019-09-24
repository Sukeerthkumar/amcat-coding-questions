# Program to find lcm of two numbers

def gcd(x, y):
    if x == 0: 
        return y
    return gcd(y%x, x)

def lcm(x, y):
    hcf = gcd(x, y)
    return (x * y) // hcf

l = [int(x) for x in input('Enter two numbers: ').split()]
lcm = lcm(l[0], l[1])
print('LCM of ' + str(l[0]) + ' and ' + str(l[1]) + ' is: ' + str(lcm))
