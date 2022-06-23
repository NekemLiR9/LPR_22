#basic rock paper scissor game

import os
import random

#Title etc.
os.system('cls||clear')
print("Number Guesser")
print("")

options = ["rock", "paper", "scissor"]

opponents_option = options[random.randint(0,2)]

answer = input("rock, paper or scissor?: ")

#"game" logic
if answer == opponents_option:
    print("draw")
elif opponents_option == options[2] and answer == options[0]:
    print("you won")
elif opponents_option == options[2] and answer == options[1]:
    print("you lost")
elif opponents_option == options[0] and answer == options[2]:
    print("you lost")
elif opponents_option == options[0] and answer == options[1]:
    print("you won")
elif opponents_option == options[1] and answer == options[2]:
    print("you won")
elif opponents_option == options[1] and answer == options[0]:
    print("you lost")
else:
    print("something went wrong")

print("")
print("your opponent chose: " + str(opponents_option))