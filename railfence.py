text = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

result = ""

for r in range(rails):
    for i in range(r, len(text), 2 * (rails - 1)):
        result += text[i]

        j = i + 2 * (rails - r - 1)

        if r != 0 and r != rails - 1 and j < len(text):
            result += text[j]

print("Encrypted:", result)