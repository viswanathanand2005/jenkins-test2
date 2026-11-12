
key = input("Enter 4 letter key: ").upper()
text = input("Enter plaintext: ").upper().replace(" ", "")


# Key matrix
a = ord(key[0]) - 65
b = ord(key[1]) - 65
c = ord(key[2]) - 65
d = ord(key[3]) - 65

det = (a * d - b * c) % 26

# Find modular inverse of determinant
det_inv = None

for i in range(26):
    if (det * i) % 26 == 1:
        det_inv = i
        break

if det_inv is None:
    print("Invalid key")
    exit()

# Make plaintext even
if len(text) % 2 != 0:
    text += "X"

encrypted = ""

for i in range(0, len(text), 2):

    x = ord(text[i]) - 65
    y = ord(text[i + 1]) - 65

    p = (a * x + b * y) % 26
    q = (c * x + d * y) % 26

    encrypted += chr(p + 65)
    encrypted += chr(q + 65)

print("Encrypted:", encrypted)


# Inverse key matrix
ia = (d * det_inv) % 26
ib = (-b * det_inv) % 26
ic = (-c * det_inv) % 26
id = (a * det_inv) % 26


# Decryption
decrypted = ""

for i in range(0, len(encrypted), 2):

    x = ord(encrypted[i]) - 65
    y = ord(encrypted[i + 1]) - 65

    p = (ia * x + ib * y) % 26
    q = (ic * x + id * y) % 26

    decrypted += chr(p + 65)
    decrypted += chr(q + 65)

print("Decrypted:", decrypted)