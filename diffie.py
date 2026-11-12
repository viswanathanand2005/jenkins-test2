p = int(input('Enter a prime number here: '))
alpha = int(input('Enter a primitive root here: '))

xa = int(input("Enter A\'s Private key here: "))
xb = int(input("Enter B\'s Private key here: "))

ya = pow(alpha,xa,p)
yb = pow(alpha,xb,p)

key1 = pow(yb, xa, p)
key2 = pow(ya, xb, p)

print(xa)
print(xb)

print(ya)
print(yb)

print(key1)
print(key2)