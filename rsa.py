import math

p = int(input('Enter a prime number (p) here: '))
q = int(input('Enter a prime number (q) here: '))

M = int(input('Enter plain text here: '))

n = p * q
totient = (p - 1) * (q - 1)

e = 2
while True:
    if math.gcd(e, totient) == 1:
        break
    e += 1
d = pow(e, -1, totient)

C = pow(M, e, n)
m = pow(C, d, n)

print(f'Original: {M}')
print(f'Encrypted: {C}')
print(f'Decrypted: {m}')