print("Welcome to the Quiz")

player = input("What's your name? ")

print("Hey " + player + "!")

start = input("Do you wanna play? ")

if start.lower() == "yes" :
    print("Okay, here we go!")
else: 
    print("Sorry to hear that...")
    quit()

score = 0

question1 = input("Who wears a red and blue suit and throw webs? a) Iron Man b) Wonderwoman c) Batman d) Spiderman ")
if question1.lower() == "d":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

question1 = input("Who played the drummer for the Beatles? a) John Lennon  b) Ringo Starr  c) Paul McCartney d) George Harrison ")
if question1.lower() == "b":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

question1 = input("What animal is the Mascot for Frosties Cereal? a) Lion  b) Tiger c) Monkey  d) Wolf ")
if question1.lower() == "b":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

question1 = input(" How many stars are within 1 light year of the Earth? a) 100 b) 1 c) 1000  d) 0 ")
if question1.lower() == "b":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

question1 = input("What is 5 cubed? a) 125  b) 25  c) 5  d) 155 ")
if question1.lower() == "a":
    print("Correct! ")
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions right!")
print("You got " + str((score/5) * 100) + "%" )