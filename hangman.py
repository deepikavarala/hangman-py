# Stage 4
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
a = random_word[0:3]
b = ("-" * (len(random_word) - 3))
print("H A N G M A N")
print("Guess the word " + random_word[0:3] + b + ":")
word = input()
if word == random_word:
    print("You survived!")
else:
    print("You are hanged!")
