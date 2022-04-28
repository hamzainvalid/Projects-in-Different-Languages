import random
import re

def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Your guess must have exactly one character.")
        elif not guess.islower():
            print("Your guess should be a lowercase letter.")
        else:
            return guess

def update_dashes(word, dashes, guess):
    counter = 0
    if re.search(guess, word):
        for i in word:
            if i == guess:
                counter+=1
        if counter > 1:
            for j in range(0,len(dashes)):
                if word[j] == guess:
                    dashes = dashes[:j] + guess + dashes[j+1:]
        x = word.find(guess)
        dashes = dashes[:x] + guess + dashes[x+1:]
    return dashes


words = ["ahmehd", "hello", "palay"]
secret_word = random.choice(words)
dashes = "-" * len(secret_word)
guesses_left = 10


while guesses_left > 0:
    print(dashes)
    print(str(guesses_left) + " incorrect guesses left.")

    guess = get_guess()
    dashes = update_dashes(secret_word, dashes, guess)
    if guess in secret_word:
        print("That letter is in the secret word.")
    else:
        print("That letter is not in the secret word.")
    if dashes == secret_word:
        break
    guesses_left -= 1


if guesses_left == 0:
    print("you lose, the word was: " + secret_word)
elif dashes == secret_word:
    print ("Congrats! You win. The word was: " + secret_word)