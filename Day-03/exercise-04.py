# Dont change the code below

print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

total_bill = 0

if size == "S": 
    total_bill += 15
    if add_pepperoni == "Y":
        total_bill += 2
elif size == "M": 
    total_bill += 20
    if add_pepperoni == "Y":
        total_bill += 3
elif size == "L":
    total_bill += 25
    if add_pepperoni == "Y":
        total_bill += 3

if extra_cheese == "Y":
        total_bill += 1

print(f"Your final bill is ${total_bill}")