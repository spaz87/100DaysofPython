import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("Select rock, paper or scissors.").lower()

options = [rock, paper, scissors]

cmp_choice_int = random.randint(0, 2)

cmp_choice = options[cmp_choice_int]

if user_choice == "rock":
    if cmp_choice == scissors:
        print(str(cmp_choice) + "User wins!")
    else: print(str(cmp_choice) + "Computer Wins!")
if user_choice == "paper":
    if cmp_choice == rock:
        print(str(cmp_choice) + "User WINS!")
    else: print(str(cmp_choice) + "Computer Wins!")
if user_choice == "scissors":
    if cmp_choice == paper:
        print(str(cmp_choice) + "USER wins!!")
    else: print(str(cmp_choice) + "Computer wins!!")

