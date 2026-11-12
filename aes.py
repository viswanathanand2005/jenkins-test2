from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

key = input('Enter a 16 character key here: ').encode()
text = input('Enter plaintext here: ').encode()

aes = AES.new(mode=AES.MODE_ECB,key=key)

encrypted = aes.encrypt(pad(text,16))
decrypted = unpad(aes.decrypt(encrypted),16)

print(f'Encrypted: {encrypted}')
print(f'Decrypted: {decrypted.decode()}')
