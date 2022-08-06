print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("Your journey begins at a crossroads. To the left is the path less travled. To the right you can see the castle in the distance.""Which path do you choose? Left or Right?").lower()

if choice1 == "left":
    choice2 = input("As you travel down the path you hear the ominus cry of a siren. Through the mist a lake appears before you. You are faced with a choice. Do you swim or do you turn back?").lower()
    if choice2 == "swim":
        choice3 = input("You swam. You have chosen the hard path and you are better for it. In life this opens many doors for you. Now you are presented with three doors. Yellow, blue, and green. Which do you choose?").lower()
        if choice3 == "yellow":
            print("You have found the dragon's hoard of gold. Prepair for battle.")
        elif choice3 == "blue":
            print("The fair maiden awaits.")
        elif choice3 == "green":
            print("Vile fumes fill the air. You are paralized and fall to the ground. You slowly fade away. Doing the right thing is not always rewarded.")
        else: print("Failure to choose is the folly of lesser men. You recive no reward.")
    else: print("The road back is a hard one. You die of the eliments.")
else:("While traveling you step in a pothole causing you to fall and hit your head. Bandits find you and take you as their slave. You die a slave.")

