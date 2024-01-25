import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)

chosen_word = random.choice(word_list)
lives = 6

# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You've already guessed {guess}.")

    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You have {lives} lives left.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
  