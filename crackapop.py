import hashlib
import os
import chardet

def test_apop(challenge, hash, wordlist_path):
    with open(wordlist_path, 'rb') as file:
        raw = file.read()
        encoding = chardet.detect(raw)['encoding']
    with open(wordlist_path, 'r', encoding=encoding) as wordlist_file:
        for password in wordlist_file:
            password = password.strip()
            test_hash = hashlib.md5((challenge + password).encode()).hexdigest()
            if test_hash == hash:
                return password
    return None

wordlist_path1 = input("Please provide a wordlist's path: ")

if not os.path.exists(wordlist_path1):
    print("File not found.")
else:
    challenge1 = input("Please provide the challenge  (e.g. <1896.697170952@server.com>): ")
    hash1 = input("Please provide the hash: ")

    print("You provided ", challenge1, " as challenge, and ", hash1," as hash.")

    result = test_apop(challenge1, hash1, wordlist_path1)
    if result:
        print(f"PASSWORD FOUND: {result}")
    else:
        print("Password not found...")
