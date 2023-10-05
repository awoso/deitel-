import random

guessed_number = random.randint(1, 40)
print(guessed_number)
guess = int(input("Enter your guess number: "))
while guessed_number != guess:
    guess = int(input("Enter your guess number: "))
print('congratulations!!!!you are the lucky winner')

