# Python RPG

import sys
import time
import os

screen_width = 100

# MAP
"""
a0, a1...
~~~~~~~~~~~~~
|  |  |  |  | a4
~~~~~~~~~~~~~
|  |  |  |  | b4
~~~~~~~~~~~~~
|  |  |  |  |
~~~~~~~~~~~~~
|  |  |  |  |
~~~~~~~~~~~~~

"""
ZONE = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False

NORTH = 'up', 'north'
SOUTH = 'down', 'south'
EAST = 'right', 'east'
WEST = 'left', 'west'

solved_places = {
    'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False,
    'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False,
    'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False,
    'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False,
}

zonemap = {
    'a1' : {
        ZONE : '',
        DESCRIPTION : 'Village Entrance',
        EXAMINATION : 'examine',
        SOLVED : False,
        NORTH : '',
        SOUTH : 'b1',
        EAST : 'a2',
        WEST : '',
    },
    'a2' : {
        ZONE : '',
        DESCRIPTION : 'Market',
        EXAMINATION : 'examine',
        SOLVED : False,
        NORTH : '',
        SOUTH : 'b2',
        EAST : 'a3',
        WEST : 'a1',
    },
    'a3' : {
        ZONE : '',
        DESCRIPTION : 'Health Center',
        EXAMINATION : 'examine',
        SOLVED : False,
        NORTH : '',
        SOUTH : 'b3',
        EAST : 'a4',
        WEST : 'a2',
    },
    'a4' : {
        ZONE : '',
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        NORTH : '',
        SOUTH : 'b4',
        EAST : '',
        WEST : 'a3',
    },
    'b1' : {
        ZONE : '',
        DESCRIPTION : 'Bank',
        EXAMINATION : 'examine',
        SOLVED : False,
        NORTH : 'a1',
        SOUTH : 'c1',
        EAST : 'b2',
        WEST : '',
    },
    'b2' : {
        ZONE : 'Home',
        DESCRIPTION : 'This is your home',
        EXAMINATION : 'Nothing has changed, your home looks the same',
        SOLVED : False,
        NORTH : 'a2',
        SOUTH : 'c2',
        EAST : 'b3',
        WEST : 'b1',
    },
    'b3' : {
        ZONE : '',
        DESCRIPTION : 'Townsmith',
        EXAMINATION : 'examine',
        SOLVED : False,
        NORTH : 'a3',
        SOUTH : 'c3',
        EAST : 'b4',
        WEST : 'b2',
    },
    'b4' : {
        ZONE : '',
        DESCRIPTION : 'TownHall',
        EXAMINATION : 'examine',
        SOLVED : False,
        NORTH : 'a4',
        SOUTH : 'c4',
        EAST : '',
        WEST : 'b3',
    },

}

movement = {
    "north" : "Go North",
    "south" : "Go South",
    "east" : "Go East",
    "west" : "Go West"
}

commands = {
    'play' : "Start the game",
    'help' : "To look for help",
    'quit' : "Get back to reality",
}

class player:
    def __init__(self):
        self.name = ''
        self.player_class = ''
        self.hp = 0
        self.mp = 0
        self.hp_regen = 0
        self.mp_regen = 0
        self.status = []
        self.location = 'b2'
        self.game_over = False

myPlayer = player() # Object

def help():
    print("#Commands: ")
    for i in commands:
        print(i, " : ", commands[i])
    
    print()
    print("Good luck and have fun!")

def look(cmd):
    print(cmd, " :", movement[cmd] )

def setup(): # Get name and class
    os.system('cls')
    class_options = ['warrior', 'mage', 'assasin', 'dark_elf']
    questions = [
        "Welcome to the Python Based Text RPG." + "\n" + "Please enter your name!\n",
        "Now it's the time to select your role!\n",
        "You can play as " + str(class_options) + ".\n",
    ]

    for character in questions[0]:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    myPlayer.name = input("=> ")

    # Role
    for character in questions[1]:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)

    def ask(): 
        for character in questions[2]:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
    
    ask()
    role = input("=> ")
    while role.lower() not in class_options:
        print("Not a valid choice! Try again!")
        ask()
        role = input("=> ")

    myPlayer.player_class = role.lower()
    print("You're a " + role + " now!")

    # Player Stats
    if role is 'warrior':
        myPlayer.hp = 150
        myPlayer.mp = 40
        myPlayer.hp_regen = 3
        myPlayer.mp_regen = 1
    elif role is 'mage':
        myPlayer.hp = 100
        myPlayer.mp = 60
        myPlayer.hp_regen = 1
        myPlayer.mp_regen = 4
    elif role is 'assassin':
        myPlayer.hp = 130
        myPlayer.mp = 50
        myPlayer.hp_regen = 2
        myPlayer.mp_regen = 3
    elif role is 'dark_elf':
        myPlayer.hp = 160
        myPlayer.mp = 60
        myPlayer.hp_regen = 1
        myPlayer.mp_regen = 1
    
    # Introduction of the player
    ask = "Hello, " + myPlayer.name + ", the " + myPlayer.player_class + "!\n\n"
    for character in ask:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    speech = [
        "Welcome to this fantasy worl....Ahhh!!\n",
        "Well, greetings will've to wait. We're under attack!!\n",
        "Let me just quickly show you around and then you may join us...",
    ]

    # i = 0
    # while i in range(3):
    #     for character in speech[i]:
    #         sys.stdout.write(character)
    #         sys.stdout.flush()
    #         time.sleep(0.02)

    for character in speech[0]:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in speech[1]:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in speech[2]:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    
    time.sleep(0.05)

    os.system('cls')

    main_game_loop()

def screen_selection():
    options = ["play", "help", "look", "quit"]
    time.sleep(0.2)
    while True:
        ip = input("=> ")
        ip = ip.split()
        option = ip[0]

        if option.lower() == options[0]: #play
            setup() # start game
        elif option.lower() == options[1]: # help
            help()
        elif option.lower() == options[2]: #look
            if len(ip) > 2:
                print("Invalid no. of inputs")
                continue
            look(ip[1])
        elif option.lower() == options[3]: #exit
            print("Hope to see you again!")
            sys.exit()
        else:
            print("Invalid Command!!")
            print("Type 'help' for help")
            continue

def screen():
    os.system('cls')
    # something for the title screen
    print('##################################################################################')
    print()
    print("                      --->Python Based Text RPG<---                               ")
    print("                           ___                                                    ")
    print("                          ( ((                                                    ")
    print("                           ) ))                                                   ")
    print("  .::.                    / /(                                                    ")
    print(" 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._    ")
    print("(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>  ")
    print(" `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''     ")
    print("  `::'                    \ \(                                                    ")
    print("                           ) ))                                                   ")
    print("                          (_((                                                    ")
    print()
    print("                                   --Play--                                       ")
    print("                                   --Help--                                       ")
    print("                                   --Quit--                                       ")
    print('##################################################################################')

    screen_selection()

def print_location():
    print()
    print('#' * (4 + len(myPlayer.location)))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print()
    print('#' * (4 + len(myPlayer.location)))

def player_move(option):
    que = "Where'd you like to go?\n"
    destination = input(que).lower()

    if destination in ['north', 'up']:
        dest = zonemap[myPlayer.location][NORTH]
        movement_handler(dest, destination)
    elif destination in ['down', 'south']:
        dest = zonemap[myPlayer.location][SOUTH]
        movement_handler(dest, destination)
    elif destination in ['right', 'east']:
        dest = zonemap[myPlayer.location][EAST]
        movement_handler(dest, destination)
    elif destination in ['lest', 'west']:
        dest = zonemap[myPlayer.location][WEST]
        movement_handler(dest, destination)

def player_examine(option):
    if zonemap[myPlayer.location][SOLVED]:
        print("You've already completed tasks in this zone!")
    else:
        print("Tasks are yet remaining. Get cracking!")

def movement_handler(destination, direction):
    if destination == '':
        print("You cannot go " + direction)
        return
    print("\n" + "You've moved to the " + zonemap[destination][DESCRIPTION] + ".")
    myPlayer.location = destination

def main_game_loop():
    while myPlayer.game_over == False:
        prompt()

def cmd_list():
    game_options = ['move', 'go', 'travel', 'quit', 'walk', 'examine', 'look', 'inspect']

    print("You have the following list of commands: ")   
    for cmd in game_options:
        print('#' + cmd)

def prompt():
    print()
    print('-' * 15)
    game_options = ['move', 'go', 'travel', 'quit', 'walk', 'examine', 'look', 'inspect', 'help']
    print("What would you like to do next?")
    option = input("> ")
    
    while option.lower() not in game_options:
        print("Unacceptable command. Please try again!")
        option = input("> ")
    if option.lower() == 'quit':
        print("Hope to see you again!")
        sys.exit()
    elif option.lower() == 'help':
        cmd_list()
    elif option.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(option.lower())
    elif option.lower() in ['examine', 'inspect', 'look']:
        player_examine(option.lower())

screen()