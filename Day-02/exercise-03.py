#Dont change the code below
age = input("What is your current age: \n")

# Write your code below this line

age = float(age)
days_in_year = 365
weeks_in_year = 52
months_in_year = 12
life_expectancy = 90

# DAYS REMAINING

days_expected = 365 * 90
days_lived = age * days_in_year
days_remaining = int(days_expected - days_lived)

# WEEKS REMAINING

weeks_expected = 52 * 90
weeks_lived = age * weeks_in_year
weeks_remaining = int(weeks_expected - weeks_lived)

# MONTHS REMAINING

months_expected = 12 * 90
months_lived = age * months_in_year
months_remaining = int(months_expected - months_lived)

print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")