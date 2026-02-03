import string

# ----- Some Hints -----
# This will give you a string with all the lowercase letters in the alphabet
alphabet = string.ascii_lowercase
print(f"{alphabet = }")

# You can look up the index of a letter in the alphabet like this:
index = alphabet.index("a")
print(f"position of 'a' in the alphabet: {index}")

# The computer already thinks of all the characters it can print out as numbers.
# If you want to, you can look up what number a character corresponds to in
# "ASCII" encoding:
ascii_number = ord("a")
print(f"ascii number representation of 'a': {ascii_number}")

ascii_letter = chr(97)
print(f"ascii letter at position #97: {ascii_letter}")

# ----- Your Algorithm -----

# Your task is to encrypt this secret message into ciphertext
plaintext = "This is a secret message."

# Initialize your ciphertext an empty string
ciphertext = ""
ciphertext2 = " "
for character in plaintext:
    encrypted_character = ord(character)
    encrypted_character += 1
    encrypted_character = chr(encrypted_character)

    ciphertext += encrypted_character

    if character in "aeiou":
        encrypted_character = "*"
    else:
        encrypted_character = character


    ciphertext2 += encrypted_character

print(f"{ciphertext = }")
print(f"{ciphertext2 = }")
