print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age? \n"))
bill = 0


if height >= 120: 
    print("You can ride the rollercoaster!") 
    if age < 12: 
         bill = 5
         print(f"Please pay ${bill}.")
    elif age <= 18: 
        bill = 7
        print(f"Please pay ${bill}.")

    elif age >= 45 and age <= 55: 
        print("Everything is going to be ok. Have a free ride on us.")
    else: 
        bill = 12
        print(f"Please pay ${bill}.")

    wants_photo = input("Do you want a photo taken? Y or N ")   

    if wants_photo == "Y":
        bill += 3 
        print(f"Your final bill is {bill}")
else:  
    print("Sorry, you have to grow taller before you can ride.")