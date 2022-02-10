count=2

while True:
    master_pwd = input("What is the master password? ")

    if count==0:
        print("You are locked out!")
        quit()
    elif master_pwd != "cats":
        print("wrong password,", count, "more guesses, then you are locked out!")
        count-=1
    else:
        print("Welcome user")
        break




def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line
            user, passw = data.split("|")
            print ("Username:", user, "| Password:", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

def wipe():
    file = open('password.txt', 'w')
    file.close()
    print("Passwords cleared")

while True:
    mode = input("Would you like to add, clear all or view passwords(add/ clear/ view), or Q to quit?  ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "clear":
        wipe()