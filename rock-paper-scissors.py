import random

user_wins = 0
comp_wins = 0

options=["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock, Paper or Scissors, or Q to quit. ").lower()
    if user_input == "q":
        break
    
    ran_num = random.randint(0, 2)
    comp_input = options[ran_num]

    if comp_input == user_input:
        print("Draw, try again!")
        continue
    elif user_input=="rock" and comp_input=="scissors":
        print("You win!")
        user_wins+=1
        continue
    elif user_input=="paper" and comp_input=="rock":
        print("You win!")
        user_wins+=1
        continue
    elif user_input=="scissors" and comp_input=="paper":
        print("You win!")
        user_wins+=1
        continue
    else :
        print("Computer Wins :(")
        comp_wins+=1
        continue

print("Player wins:", user_wins)
print("Computer wins:", comp_wins)
print("Come back soon!")