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

cross_road = input("You are at a cross road. Where do you want to go? left or right? \n").lower()

if cross_road == "right": 
    print("You entered the road of bandits. Game over! \n")
elif cross_road == "left":
    island = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' for a boat. Type 'swim' to swim accross \n").lower()
    if island == "swim": 
        print("There're sharks in the lake. Game over! \n")
    elif island == "wait":
        house = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow and blue one. Which color do you choose? \n").lower()
        if house == "red" or house == "blue" : 
            print("The house you entered is full of beasts. Game over! \n")
        elif house == "yellow" : 
            print("Hurray!!! You win")

    