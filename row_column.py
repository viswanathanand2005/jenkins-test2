text = input("Enter plaintext: ").replace(" ", "")
key = input("Enter key: ")

cols = len(key)

# Padding
while len(text) % cols != 0:
    text += "X"

# Create matrix
matrix = []

for i in range(0, len(text), cols):
    matrix.append(list(text[i:i+cols]))

# Get column order
order = sorted(range(cols), key=lambda x: key[x])

# Read columns
result = ""

for col in order:
    for row in matrix:
        result += row[col]

print("Encrypted:", result)