# Guess the number game
# create a random number between 1 and 100
# ask the user to guess the number
# if the guess is too high, tell the user
# if the guess is too low, tell the user
# if the guess is correct, tell the user and end the game
# keep track of the number of guesses
import random


numbers = random.randint(1, 100)
guess = 0
while guess !=numbers:
    guess = int(input("enter a number between 1 and 100:"))
    if guess > numbers:
            print( "too High")
    elif guess < numbers:
            print("too low")
(print ("You win skibidi sigma"))

