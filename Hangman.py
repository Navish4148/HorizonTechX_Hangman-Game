import os
import random

MAX_INCORRECT_GUESSES = 6
WORD_BANK = ["python", "hangman", "developer", "program", "code"]

HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

def clear_screen():
    """Clears the terminal for a cleaner visual interface."""
    os.system("cls" if os.name == "nt" else "clear")

def get_valid_guess(guessed_letters):
    """Prompt the player until they enter a single, un-guessed letter."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter (A–Z).\n")
        elif guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try another!\n")
        else:
            return guess

def display_board(secret_word, guessed_letters, incorrect_guesses):
    """Renders the gallows, word progress, and guessed letters cleanly."""
    clear_screen()
    print("====================================")
    print("        WELCOME TO HANGMAN!         ")
    print("====================================\n")

    print(HANGMAN_PICS[incorrect_guesses])
    print()

    word_display = [
        letter if letter in guessed_letters else "_" for letter in secret_word
    ]
    print(f"Word:      {' '.join(word_display)}")
    print(
        f"Guessed:   {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
    )
    print(
        f"Attempts:  {MAX_INCORRECT_GUESSES - incorrect_guesses} remaining\n"
    )

    return "_" not in word_display

def play_round():
    """Manages a single match of Hangman."""
    secret_word = random.choice(WORD_BANK)
    guessed_letters = set()
    incorrect_guesses = 0

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        is_won = display_board(secret_word, guessed_letters, incorrect_guesses)

        if is_won:
            print("🎉 Congratulations! You guessed the secret word!")
            return

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in secret_word:
            incorrect_guesses += 1

    display_board(secret_word, guessed_letters, incorrect_guesses)
    print("====================================")
    print(f"💀 GAME OVER! The secret word was: '{secret_word}'")
    print("====================================")

def main():
    """Main game loop for replay management."""
    while True:
        play_round()
        replay = input("\nPlay again? (y/n): ").lower().strip()
        if replay != "y":
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()