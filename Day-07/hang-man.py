import random
from hangman_art import logo, stages
from hangman_words import word_list

# Step 1
print(logo)
lives = 6

random_position = random.randint(0, len(word_list) - 1)
# random.choice(word_list)
chosen_word = word_list[random_position]
chosen_letters = list(chosen_word)
letters_length = len(chosen_letters)

# Step 2

display = []
blank = "_"
guessed_letters = ""

for letter in chosen_letters:
    display += "_"

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed letter {guess}")

    for position in range(letters_length):
        letter = chosen_letters[position]
        if guess == chosen_letters[position]:
            display[position] = letter
    
    guessed_letters += guess

    print(f"{" ".join(display)}")


    if blank not in display:
        print("You win")
        game_over = True

    if guess not in chosen_letters:
        print(f"You guessed '{guess}', that's not in the word! You lose a life!")
        print(stages[lives])
        if lives != 0: 
            lives -= 1
        else: 
            print("You lose")
            print(chosen_word)
            game_over = True
            