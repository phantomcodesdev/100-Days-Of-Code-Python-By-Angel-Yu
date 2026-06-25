# Dont change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your name \n")

# Write your code below this line
name1 = name1.lower()
name2 = name2.lower()

names = name1 + name2

first_digit = names.count("t") + names.count("r") + names.count("u") + names.count("e")
second_digit = names.count("l") + names.count("o") + names.count("v") + names.count("e")

score = int(f"{first_digit}{second_digit}")

if score < 10 or score > 90: 
    print(f"Your score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")