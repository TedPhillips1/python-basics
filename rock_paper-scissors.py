import random

comp_wins = 0
user_wins = 0 

options = ["rock", "paper", "scissors"]

while True: 
    user_input = input("Choose rock, paper, scissors or q to quit ").lower()
    if user_input == "q":
        break
    random_num = random.randint(0, 2)
    comp_input = options[random_num]
    if user_input == comp_input:
        print("Draw")
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

print("Congratulations you won" , user_wins , "times!" )
print ("The computer won" , comp_wins , "times!")
print("so long")









