from email.headerregistry import ContentTypeHeader


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for letter in plain_text:
        posistion = alphabet.index(letter)
        new_posistion = posistion + shift_amount
        new_letter = alphabet[new_posistion]
        encoded_text += new_letter
    print(f"The encoded text is {encoded_text}")

def decrypt(plain_text, shift_amount):
    decoded_text = ""
    for letter in plain_text:
        posistion = alphabet.index(letter)
        new_posistion = posistion - shift_amount
        new_letter = alphabet[new_posistion]
        decoded_text += new_letter
    print(f"Your decoded text is {decoded_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else: print(f"Only encrypt and decrypt are options. You chose {direction}")