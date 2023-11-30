import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple", "blueberry", "kiwi", "mango"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
            if attempts == 0:
                print("Sorry, you lost! The word was:", word_to_guess)
                break
        else:
            displayed = display_word(word_to_guess, guessed_letters)
            print(displayed)
            if '_' not in displayed:
                print("Congratulations! You guessed the word:", word_to_guess)
                break

if __name__ == "__main__":
    hangman()
