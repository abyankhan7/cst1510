# Week 4 — Extra Practice Projects

## Banker Roulette
import random
friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]
payer = random.choice(friends)
print(f"{payer} is paying the bill today")
num_friends = len(friends)
index = random.randint(0, num_friends - 1)
payer = friends[index]
print(f"{payer} is paying the bill today")

## Password Generator
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
up_letters = []
for letter in letters:
    up_letters.append(letter.upper())
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
nr_letters = int(input("How many letters would you want: "))
nr_symbols = int(input("How many symbols would you want: "))
nr_numbers = int(input("How many numbers would you want: "))
password = ""
for i in range(nr_letters):
    password += random.choice(letters)
for s in range(nr_symbols):
    password += random.choice(symbols)
for n in range(nr_numbers):
    password += str(random.choice(numbers))
print(password)
password_list = []
for i in range(nr_letters):
    password_list.append(random.choice(letters))
for s in range(nr_symbols):
    password_list.append(random.choice(symbols))
for n in range(nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = "".join(password_list)
print(password)

# ## Blind Auction
bids = {}
keep_bidding = True
while keep_bidding:
    name = input("What the bidders  name: ")
    bid = int(input("What is your bid : "))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bidders == "no":
        keep_bidding = False
    else:
        print("\n" * 1)
highest_bid = 0
winner = ""
for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name
print(f"The winner is {winner} with a bid of £{highest_bid}.")

# ## Coffee Machine
resources = {"water": 300, "milk": 200, "coffee": 100}
MENU = {
        "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
        "latte":    {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
        "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

def report():
    for resource in resources.items():
        print(f"{resource[0]}: {resource[1]}")
def is_resource_sufficient(ingredients):
    for item, amount in ingredients.items():
        if amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
def make_coffee(drink_name, ingredients):
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")
machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report()
    else:
        drink = MENU.get(choice)
        if drink == "None":
            print("Sorry, that's not on the menu.")
        else:
            result = is_resource_sufficient(drink["ingredients"])
            if result == True:
                print(drink["cost"])
                payment = float(input("How much do you want to pay? "))
                if payment >= drink["cost"]:
                    change = round(payment - drink["cost"], 2)
                    print(change)
                    make_coffee(choice, drink["ingredients"])
                print("Sorry, that's not enough money. Money refunded.")









