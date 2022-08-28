from art import logo 
import os 

print(logo)

end_bidding = False
bids = []

while not end_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    new_bid = {
        "Bidder name": name,
        "Bid amounts": bid,
    }
    bids.append(new_bid)
    next_bidder = input("Would other users like to bid? /n If yes type 'yes'. If no type 'no'.").lower()
    if next_bidder == "no":
        end_bidding = True
    os.system('clear')

high_bidder = ""
high_bid = 0

for b in bids:
    if b["Bid amounts"] >= high_bid:
        high_bidder = b["Bidder name"]
        high_bid = b["Bid amounts"]

print(f"The winner is {high_bidder} with a bid of ${high_bid}.")



    

