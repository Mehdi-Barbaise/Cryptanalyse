# Import required modules
import argparse
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad
import base64

def decrypt_3des(ciphertext_b64, key, iv):
    """Decrypt 3DES ciphertext."""
    # Decode base64 ciphertext
    ciphertext = base64.b64decode(ciphertext_b64)
    
    # Create 3DES cipher (CBC mode)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    
    # Decrypt and remove padding
    decrypted = unpad(cipher.decrypt(ciphertext), DES3.block_size)
    
    # Extract last 12 bytes (expected plaintext length)
    expected_length = 12
    return decrypted[-expected_length:].decode('utf-8')

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Decrypt Roundcube 3DES")
    parser.add_argument('--ciphertext', required=True, help="Base64 ciphertext")
    parser.add_argument('--key', required=True, help="24-byte key in hex (48 chars)")
    parser.add_argument('--iv', required=True, help="8-byte IV in hex (16 chars)")
    args = parser.parse_args()
    
    # Convert inputs to bytes
    try:
        # Convert hex key to bytes (expects 48 chars for 24 bytes)
        key = bytes.fromhex(args.key)
        if len(key) != 24:
            raise ValueError(f"Key must be 24 bytes (48 hex chars), got {len(key)} bytes")
        # Convert hex IV to bytes (expects 16 chars for 8 bytes)
        iv = bytes.fromhex(args.iv)
        if len(iv) != 8:
            raise ValueError(f"IV must be 8 bytes (16 hex chars), got {len(iv)} bytes")
        
        # Decrypt and print result
        result = decrypt_3des(args.ciphertext, key, iv)
        print("Decrypted:", result)
    except ValueError as e:
        print("Error:", str(e))
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()