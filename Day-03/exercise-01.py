# Dont change the code below
number = int(input("Which number do you want to check? \n"))

# Write your code below this line
divided = number / 2

if number % 2 == 0: 
    print (f"{number} is even because {number} / 2 = {round(divided)} \n {round(divided)} does not have any decimal places. Therefore the division is clean.")
else:
    print(f"{number} is odd because {number} / 2 = {divided} \n {round(divided, 3)} is not a whole number, it has decimal places. Therefore there's a remainder of {number % 2}, so the division is not clean.")