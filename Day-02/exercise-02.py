# Dont change the code below 
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Write your code below this line

height = float(height)
weight = float(weight)

BMI = int(weight / (height ** 2))
print (BMI)