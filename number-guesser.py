import os
import random

  
print("Welcome to the Random Number Guesser")
user_input = input("Give me a number: ")

if user_input.isdigit():
    if int(user_input)<=0:
        print("Pick a number bigger than 0 next time!")
        print ("Restarting...")
        os.system("python number-guesser.py")
        exit()
else: 
    print("Please type a number next time.")
    print ("Restarting...")
    os.system("python number-guesser.py")
    exit()

ran_num = random.randint(1, int(user_input))


guesses= 0

while True:
    user_guess= input("Guess a number between 1 and " + str(user_input) + ": ")
    guesses+=1
    if user_guess.isdigit():
        if int(user_guess)<=0:
            print("Pick a number bigger than 0 next time!")
            continue
        elif user_guess>user_input:
            print("Guess a number less than or equal to the one you picked originally.")
            continue
    else: 
        print("Please type a number next time.")
        continue

    if int(user_guess)==ran_num:
        print("Correct! You guessed the random number!")
        break
    elif int(user_guess)>ran_num:
        print("Too high, guess again!")
    else:
        print("Too low, guess again!")

print("It took you", guesses, "guesses!")

play_again=input("Do you want to play again? (yes/no) ")
if play_again.lower()=="yes":
    print ("Restarting...")
    os.system("python number-guesser.py")
    exit()
else: 
    quit()