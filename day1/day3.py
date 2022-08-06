# 🚨 Don't change the code below 👇
from audioop import add


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25
else: print("Error")

if add_pepperoni == "Y":
    if size == "S":
        total += 2
if add_pepperoni == "Y":
    if size == "M":
        total += 3
if add_pepperoni == "Y":
    if size == "L":
        total += 3
else: print("error")

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}")