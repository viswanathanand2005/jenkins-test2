from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad

text = input('Enter plaintext here: ').encode()
key = input('Enter a 8 character key here: ').encode()

cipher = DES.new(mode=DES.MODE_ECB,key=key)

encrypted = cipher.encrypt(pad(text,8))
decrypted = unpad(cipher.decrypt(encrypted),8)

print(encrypted)
print(decrypted.decode())