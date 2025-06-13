import random

def hangman():
    word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']
    chosen_word = random.choice(word_list)
    guessed_letters = []
    tries = 6
    display = ['_' for _ in chosen_word]

    print("Welcome to Hangman!")
    print(" ".join(display))

    while tries > 0 and '_' in display:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess
            print("Correct!")
        else:
            tries -= 1
            print(f"Incorrect! You have {tries} tries left.")

        print(" ".join(display))

    if '_' not in display:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Game over! The word was '{chosen_word}'.")

if __name__ == "__main__":
    hangman()