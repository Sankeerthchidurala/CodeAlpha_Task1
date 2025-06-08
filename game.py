import random

# List of possible words for the game
WORDS = [
    "python", "programming", "hangman", "developer", "challenge",
    "function", "variable", "syntax", "algorithm", "repository"
]

MAX_ATTEMPTS = 6

def get_random_word():
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    word = get_random_word()
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("🎮 Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Incorrect guess.")
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You've guessed the word:", word)
            break
    else:
        print("\n💀 Game over. The word was:", word)

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
