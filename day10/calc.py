from art import logo
# Multiply Function
def multi(num1, num2):
    answer = num1 * num2
    print(answer)

# Divide Function
def divide(num1, num2):
    answer = num1 / num2
    print(answer)

# Addition Function 
def add(num1, num2):
    answer = num1 + num2
    print(answer)

# Subtraction 
def sub(num1, num2):
    answer = num1 - num2
    print(answer) 

# Function choice function 
def user_math(num1, num2, user_choice):
    if user_choice == "*":
        multi(num1, num2)
    elif user_choice == "/":
        divide(num1, num2)
    elif user_choice == "+":
        add(num1, num2)
    elif user_choice == "-":
        sub(num1, num2)
    else: print("You did not make an valid choice.")
    
should_end = False
print(logo)
while not should_end:
    choice1 = int(input("What is the first number? "))
    choice2 = input("""
    *
    /
    +
    -
    What operation would you like to perform? """)
    choice3 = int(input("What is the second number? "))
    user_math(choice1, choice3, choice2)
    keep_going = input("If you would like to go again enter 'y' if no enter 'n': ")
    if keep_going == "n":
        should_end = True
