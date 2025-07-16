def decode(a):
    result = []
    for i, c in enumerate(a):
        if c.isalpha():
            if c.isupper():
                base = ord('A') 
            else:
                base = ord('a')
            original_i = (ord(c) - base - i) % 26
            result.append(chr(original_i + base))
        else:
            result.append(c)

    return ''.join(result)

cipher = input("Please provide the cipher text: ")

decoded_txt = decode(cipher)

print("Here's the decoded message: ", decoded_txt)
