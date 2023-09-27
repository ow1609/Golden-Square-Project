def say_hello(name):
    return f"hello {name}"


# Intended output:
#
# > say_hello("kay")
# => "hello kay"
print(say_hello("kay"))


def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        print(ciphered_char)
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    # print(alphabet)
    cipher_with_duplicates = list(key) + alphabet
    # print(cipher_with_duplicates)
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        # print(cipher_with_duplicates[i])
        # print(cipher_with_duplicates[:i])
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            
            cipher.append(cipher_with_duplicates[i])
    # print(cipher)
    return cipher
    

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

print(f"""
 Running: encode("t", "secretkey")
Expected: E
  Actual: {encode('t', 'secretkey')}
""")


def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
    # print(counter)
    sorted_tuple_list = sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0]
    return (sorted_tuple_list)
print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")