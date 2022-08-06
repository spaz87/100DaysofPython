print("Welcome to the tip calculator.")

total = input("What was the total bill?")

tip_intput = input("What percentage tip would you like to leave?")
tip_output = int(tip_intput) / 100
tip_amount = float(total) * tip_output

number_splitting = input("How many people are splitting the bill?")

your_portion = (float(total) + tip_amount) / int(number_splitting)
your_portion_rounded = round(your_portion, 2)

print(f"Each person should pay: ${your_portion_rounded}")