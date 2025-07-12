import random
word_bank = ['bubbles','sigma','crush','squishy','squash','excuse','squabble','abstract','abscond','absolve','abstain','absurd','abundance','abuse','academic','acceptance','accessory','accident']

# to select a random word from the word bank
word = random.choice(word_bank)
# to create a list of underscores for the word
underscores = ['_'] * len(word)

# to keep track of the letters guessed
attempts = 10

while attempts > 0:
    print("Current word: ", ' '.join(underscores))
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                underscores[index] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

    if '_' not in underscores:
        print("Congratulations! You've guessed the word:", word)
        break

if attempts == 0:
    print("Sorry, you've run out of attempts. The word was:", word)