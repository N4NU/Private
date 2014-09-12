def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = input('num1:')
num2 = input('num2:')

print (hex(gcd(num1, num2)))
