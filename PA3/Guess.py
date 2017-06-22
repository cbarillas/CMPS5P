# Carlos Barillas
# cbarilla@ucsc.edu
# Programming Assignment 3
# This program generates firstGuess random integer and gives user three chances to guess the randomly # generated integer.


import random

print("I'm thinking of an integer in the range 1 to 10. You have three guesses.\n")

randomNumber = random.randint(1,10)

#First Guess
firstGuess = int(input("Enter your first guess: "))

if firstGuess <  randomNumber:
    print("Your guess is too low.\n")
elif firstGuess > randomNumber:
    print("Your guess is too high.\n")
elif firstGuess == randomNumber:
    print("You win!\n")             
    exit()                          # Exits the program once you've won.

#Second Guess
secondGuess = int(input("Enter your second guess: "))

if secondGuess < randomNumber:
    print("Your guess is too low.\n")  
elif secondGuess > randomNumber:
    print("Your guess is too high.\n")
elif secondGuess == randomNumber:
    print("You win!\n")
    exit()

#Third Guess
thirdGuess = int(input("Enter your third guess: "))

if thirdGuess < randomNumber:
    print("Your guess is too low.\n")
    print("You lose. The number was {}.\n".format(randomNumber))
elif thirdGuess > randomNumber:
    print("Your guess is too high.\n")
    print("You lose. The number was {}.\n".format(randomNumber))
elif thirdGuess == randomNumber:
    print("You win!\n")
    exit()
               
