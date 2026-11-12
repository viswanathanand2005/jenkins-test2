def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    res = ""
    i = 0
    while i < len(text):
        res += text[i]
        if i + 1 == len(text) or text[i] == text[i+1]:
            res += "X"
            i += 1
        else:
            res += text[i+1]
            i += 2
    return res

def generate_matrix(key):
    key = key.upper().replace("J", "I").replace(" ", "")
    matrix = []
    seen = set()
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c

def encrypt(text, matrix):
    cipher = ""
    for i in range(0, len(text), 2):
        r1, c1 = find_pos(matrix, text[i])
        r2, c2 = find_pos(matrix, text[i+1])
        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

matrix = generate_matrix(key)
prepared_text = prepare_text(plaintext)
print(encrypt(prepared_text, matrix))