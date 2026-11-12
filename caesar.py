text = input('Enter plaintext here: ')
shift = int(input('Enter shift here: '))

res = ''

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        new = chr(((ord(ch) - base + shift) % 26) + base)
        res += new
    else:
        res += ch

print(res)