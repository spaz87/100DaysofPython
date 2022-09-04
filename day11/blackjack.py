from art import logo
import random 

print(logo)
# Set game variables hands and cards. 
computer_hand = []
player_hand = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## Initial Draw Function 
def deal_cards(deck, hand1, hand2):
    hand1.append(random.choice(deck))
    hand1.append(random.choice(deck))
    hand2.append(random.choice(deck))
    hand2.append(random.choice(deck))

#Function for a Hit aka card draw
def add_card(deck, hand1, hand2):
    hand1.append(random.choice(deck))
    hand2.append(random.choice(deck))

#Game ending options 
def game_status(hand1, hand2):
    if sum(hand1) <= 21 and sum(hand2) <= 21:
        if sum(hand1) > sum(hand2):
            print("The dealer wins!")
        elif sum(hand1) < sum(hand2):
            print("Player wins!")
        elif sum(hand1) == sum(hand2):
            print("Dealer and player tied. House wins.")
        elif sum(hand1) > 21 and sum(hand2) > 21:
            print("All players busted. No winner")
        elif sum(hand1) > 21:
            print("The dealer has busted. Player Wins!")
        elif sum(hand2) > 21:
            print("Player busted. Dealer wins.")

#Checks for busted hands 
def status_check(hand1, hand2):
    if sum(hand1) > 21 and sum(hand2) > 21:
        print("All players busted. No winner")
    elif sum(hand1) > 21:
        print("The dealer has busted. Player Wins!")
    elif sum(hand2) > 21:
        print("Player busted. Dealer wins.")

#Checks for aces and allows the choice of a 1 or 11. 
def check_aces(hand2):
    for card in hand2:
        if card == 11:
            int(input("Aces can equal 11 or 1. Choose which you would like. Enter 11 or 1: "))
        
#Running of the game
# Phase one - dealing of cards        
deal_cards(cards, computer_hand, player_hand)
print(f"Dealer's first card: {computer_hand[0]}")
print(f" Your cards: {player_hand}")
#Game play after dealing - hitting, choosing ace value, checking for busted hands, and determine the winner. 
end_game = False 
while not end_game:
    take_card = input("Would you like to hit? Y or N  ").lower()
    if take_card == "y":
        add_card(cards, computer_hand, player_hand)
        print(f"Dealer's first card: {computer_hand[0]}")
        print(f" Your cards: {player_hand}")
        check_aces(player_hand)
        status_check(computer_hand, player_hand)
        if sum(computer_hand) >21 or sum(player_hand) >21:
            end_game = True
    elif take_card == "n":
        game_status(computer_hand, player_hand)
        end_game = True