from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()
message = input("Enter the message: ").encode("utf-8")
signature = private_key.sign(message, hashes.SHA256())
print("\nDigital Signature Generated Successfully!")
print("Signature (hex):", signature.hex())

try:
    public_key.verify(signature, message, hashes.SHA256())
    print("\nSignature Verification: SUCCESS")
    print("Message is authentic and unchanged.")

except Exception:
    print("\nSignature Verification: FAILED")

modified_message = message + b" modified"

try:
    public_key.verify(signature, modified_message, hashes.SHA256())
    print("Modified Message: Verification SUCCESS")

except Exception:
    print("Modified Message: Verification FAILED")
