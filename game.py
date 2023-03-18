import random

def generate_word():
    words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape", "honeydew", "imbe", "jackfruit"]
    return random.choice(words)

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    print("Welcome to Word Scramble!")
    print("Unscramble the word and enter your answer.")

    word = generate_word()
    scrambled_word = scramble_word(word)

    print("Scrambled word:", scrambled_word)

    while True:
        guess = input("Enter your guess: ")
        if guess == word:
            print("Congratulations, you unscrambled the word!")
            break
        else:
            print("Sorry, that's not correct. Try again.")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing Word Scramble!")

play_game()
