import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, user_direction):
    if user_direction == "encode":
        encoded_text = ""
        for letter in plain_text:
            if letter in alphabet:
                posistion = alphabet.index(letter)
                new_posistion = (posistion + shift_amount) % 26
                new_letter = alphabet[new_posistion]
                encoded_text += new_letter
            else: encoded_text += letter 
        print(f"The encoded text is: {encoded_text}")
    elif user_direction == "decode":
        decoded_text = ""
        for letter in plain_text:
            if letter in alphabet:
                posistion = alphabet.index(letter)
                new_posistion = (posistion - shift_amount) % 26
                new_letter = alphabet[new_posistion]
                decoded_text += new_letter
            else: decoded_text += letter
        print(f"Your decoded text is: {decoded_text}")

should_end = False 
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift, user_direction=direction)
    restart = input("Type yes if you would like to go again. Otherwise type no.").lower()
    if restart == "no":
        should_end = True
        print("Goodbye")