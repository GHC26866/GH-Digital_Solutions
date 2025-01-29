# Guess the number game
# create a random number between 1 and 100
# ask the user to guess the number
# if the guess is too high, tell the user
# if the guess is too low, tell the user
# if the guess is correct, tell the user and end the game
# keep track of the number of guesses
import random
numbers = random.randint(1, 100)
guesses = 0
guess = input ("Guess a number between 1 and 100: ")
if guess > numbers:
    print ("Too high")
if guess < numbers:
    print ("Too low")
if guess == numbers:
    print ("Correct")


