#Step 1 
from posixpath import split
import random
from hangman_words import word_list

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("What letter would you like to guess?: ").lower()
    guess_list = []
    guess_list += guess
    letter_list = []
    for digit in range(word_length):
        letter = chosen_word[digit]
        if letter == guess:
            display[digit] = letter
        letter_list += letter
    if guess not in letter_list:
        print(f"{guess} is not one of the letters in the word.")
        lives -= 1
        if lives == 0:
            print("You lose. Game over.")  

    print(stages[lives])
    print(display)
    print(f"These are your previous guesses: {guess_list}")
    if "_" not in display:
        end_of_game = True
        print("You win the game!")