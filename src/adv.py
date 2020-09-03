from room import Room
from player import Player
from item import Item
from treasure import Treasure
import textwrap
import time
import random

# Declare all the rooms & items
value = random.randint(10, 25)
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", []),
}

items = {
    "dagger": Item("Dagger", "A rusty old dagger, any sharpness it once had is lost to the ages."),

    "gold": Treasure("Gold", "A small pile of gold coins! May be worth something.", value),

    "torch": Item("Torch", "You aren't sure how this torch is still lit, but who are you to question it?"),

    "sword": Item("Sword", "This bronzesword surprisingly is still in good condition. Might be an effective weapon."),

    "goblet": Treasure("Goblet", "The jewels embedded in the goblet in your hands shimmer in the pale light.", 100)
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Assign items to rooms

room['outside'].ground = [items['dagger']]
room['foyer'].ground = [items['gold'], items['torch']]
room['treasure'].ground = [items['sword'], items['goblet']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player('Explorer', room['outside'])
cardinal = ['n','e','s','w']
choice = ''
entry = ''

print(textwrap.fill(f'Welcome, {player.name}. So you have come seeking treasure? \nYou may navigate with "n", "e", "s" or "w", and may pick or drop items using "g"/"get", or "d"/"drop" respectively. \nYou can end the game when you are finished with the "q" key.'))
time.sleep(3)
player.name = input("What is your name, explorer?\n").strip()
while entry != 'q':
    ground = player.location.ground
    inven = player.inventory
    exchange = len(ground) > 0
    time.sleep(1)

    print('\n\n\n', player)

    if exchange:
        print("You see these items nearby:\n")
        for item in ground:
            print(item, "\n")

    choice = input("Please choose which direction you would like to move:\n").lower().split()
    entry = choice[0]

    if len(choice) == 2:
        swap = choice[1]
        if choice[0] == "get" or choice[0] == "g":
            if exchange:
                for item in ground:
                    if swap in item.name.lower():
                        player.get(item)
                        ground.remove(item)
            else:
                print("There's nothing for you to pick up!")
        elif choice[0] == "drop" or choice[0] == "d":
            if len(inven) > 0:
                for item in inven:
                    if swap in item.name.lower():
                        player.drop(item)
                        ground.append(item)
            else:
                print("You have nothing in your inventory.")
        else:
            print("That's not a recognized command.")

    else:
        entry = choice[0]
        if entry in cardinal:
            if hasattr(player.location, f'{entry}_to'):
                player.location = getattr(player.location, f'{entry}_to')
            else:
                print("\n\n\nThere is nothing for you in that direction.") 
        elif entry == 'i':
            if len(inven) > 0:
                print('Here is your inventory:')
                for item in inven:
                    print(item.name)
            else:
                print("Your inventory is empty!")
        elif entry == 'q':
            print(f'Farewell {player.name}. Until next time. Your final score was {player.score}')    
        else:
            print('\n\nPlease select a valid direction, or press "q" if you would like to quit the game.')