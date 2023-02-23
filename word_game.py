import random

# List of words to choose from
words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

# Pick a random word
word = random.choice(words)

# Jumble the word
jumbled = "".join(random.sample(word, len(word)))

# Welcome message
print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")

# Show the jumbled word
print(f"The jumbled word is: {jumbled}")

# Get the player's guess
guess = input("Enter your guess: ")

# Keep prompting the player until they guess correctly
while guess != word:
    print("Sorry, that's not correct. Try again.")
    guess = input("Enter your guess: ")

# Congratulate the player
print("Congratulations, you guessed the word!")
