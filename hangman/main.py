import random
from art import logo
from art import stages
from words import word_list

chosen_word = random.choice(word_list)
print(logo)
print("Animal guessing game!")
lives = 6

display = []
guessed_letters = []
for letter in chosen_word:
    display.append("_")

# print(f"The solution is: {chosen_word}.")
game_on = True

while game_on:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word and guess not in guessed_letters:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess
                guessed_letters.append(guess)
    elif guess in guessed_letters:
        print(f"You have already guessed '{guess}'")
    elif guess not in chosen_word and guess not in guessed_letters:
        lives -= 1
        print(f"'{guess}' is not in the word.")
        guessed_letters.append(guess)

    print(f"{' '.join(display)}")

    if "_" not in display and lives > 0:
        game_on = False
        print("You win!")
    elif lives == 0:
        game_on = False
        print(f"You lost the game, the word was: {chosen_word}")

    print(stages[lives])

