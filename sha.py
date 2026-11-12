import hashlib
def sha256_hash(message):
    encoded_message = message.encode('utf-8')
    hash_object = hashlib.sha256(encoded_message)
    return hash_object.hexdigest()

message = input("Enter the message: ")
hash_value = sha256_hash(message)
print("\nOriginal Message:", message)
print("SHA-256 Hash:", hash_value)
print("Hash Length:", len(hash_value), "hexadecimal characters")
