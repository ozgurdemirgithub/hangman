import random

def get_word(lst):
    return lst[random.randint(0, len(lst) - 1)]

def play_hangman(word, hangman):
    tries = len(hangman)-1
    current_guess = ["_"] * len(word)

    words = []
    letters = []

    print("Welcome to Hangman!")

    while True:
        print(hangman[tries])
        print("Word: " + " ".join(current_guess))
        print("Guessed Letters: " + " ".join(letters))
        print("Guessed Words: " + " ".join(words))

        if tries == 0:
            print("You ran out of tries.")
            print("The word was " + word)
            break

        guess = input("Please guess a letter or a word: ").upper()
        if not guess.isalpha():
            print("Please enter a valid letter or word.")
            continue
        elif len(guess) == 1:  # letter
            if guess in letters:
                print("You have already guessed letter: " + guess)
            elif guess in word:
                print(guess + " is in the word!")
                letters.append(guess)

                for i in [pos for pos, char in enumerate(word) if char == guess]:
                    current_guess[i] = guess

                if "_" not in current_guess:
                    print("You win! The word is " + word + "!")
                    break
            else:
                tries -= 1
                print(guess + " is not in the word!")
                letters.append(guess)
        else:  # word
            if guess in words:
                print("You have already guessed word: " + guess)
            elif guess == word:
                print("You win! The word is " + word + "!")
                break
            elif guess != word:
                tries -= 1
                print("Your guess is wrong!")
                words.append(guess)


def main():
    play = True

    while play:

        with open("words.txt", "r") as f:
            word_list = f.readlines()
        word_list = [i.strip().upper() for i in word_list]
        word = get_word(word_list)

        with open("hangman.txt", "r") as f:
            hangman = f.read()
        hangman = hangman.split(",")
        hangman.reverse()

        play_hangman(word, hangman)

        while True:

            print("Do you wanna continue? Y/N")
            c = input().upper()

            if c == "N":
                print("Thanks for playing Hangman")
                play = False
                break
            elif c == "Y":
                print("Game is restarting!")
                play = True
                break
            else:
                print("Wrong Input! " + c)
                continue


print("I want to play a game...")
main()
