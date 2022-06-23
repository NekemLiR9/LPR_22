#Create random number and track how long it takes for the user to guess that number
#After a guess tell the user if they were below or above the number
import random
import os 

#Create random number
number = random.randint(0,10)

#variable to track tries
tries = 0
answer = 11

#ask user to guess number it until its correct
while number != answer:
    os.system('cls||clear')
    print("Number Guesser")
    print("")
    
    try:

        answer = int(input("Guess a number from 0 to 10:"))
        tries = tries + 1

        #Tell the user if they were above or below the number but only if you didnt guess the correct number
        if number != answer:

            if answer > number:
                print("the number is smaller.")
            else:
                print("the number is bigger.")
            print("")
            input("Press any key to retry ")
    except:
        print("ERROR: Incorrect syntax. Try typing a number instead.")
        print("")
        input("Press any key to retry ")

#"ui"
os.system('cls||clear')
print("Number Guesser")
print("-   -   -   -   -   -")
print("")
print("Correct!")

#tries and try correction
if tries <= 1:
    tries_grammar = "try"
else:
    tries_grammar = "tries"

print("It took you " + str(tries) + " " + tries_grammar + " to guess the correct number")

print("")
print("")
print("")