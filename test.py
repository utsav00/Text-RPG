import os
import sys
import time

def setup():
    os.system('cls')
    class_options = ['warrior', 'mage', 'assasin', 'dark_elf']
    questions = [
        "Welcome to the adventure." + "\n" + "Please enter your name!\n",
        "Now it's the time to select your role!\n",
        "You can play as " + str(class_options) + ".\n",
    ]

    for character in questions[0]:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    name = input(">")
    # myPlayer.name = input("=> ")

    def ask():
        for character in questions[1]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        
        for character in questions[2]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        
    ask()
    role = input("=> ")
    while role not in class_options:
        print("Not a valid choice! Try again!")
        role = input("=> ")
        ask()

    # myPlayer.player_class = role
    print("You're a " + role + " now!")


### Testing