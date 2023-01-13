import random
import string
adjectives = ['sleepy', 'slow', 'smelly',
              'wet', 'fat', 'red',
              'orange', 'yellow', 'green',
              'blue', 'purple', 'fluffy',
              'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda']

while True:

    print('Welcome to password picker!')

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    spec_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + spec_char

    print("your password is %s" %password)

    response = input('Would you like another password? Type y or n: ')
    if response == 'n':
        break