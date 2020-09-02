from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
valid = ['n','e','s','w']
player = Player(room['outside'])

print(textwrap.fill('You have come seeking treasure. You may select your choices with "n", "e", "s" or "w", or type "q" if you would like to end the game.', width=40))
choice = ''
while choice != 'q':
    print('\n\n\n', player)

    choice = input("Please choose which direction you would like to move: ").lower() 
    if choice in valid:
        if choice == 'n' and hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
        elif choice == 's' and hasattr(player.location, 's_to'):
            player.location = player.location.s_to         
        elif choice == 'e' and hasattr(player.location, 'e_to'):
            player.location = player.location.e_to 
        elif choice == 'w' and hasattr(player.location, 'w_to'):
            player.location = player.location.w_to 
        else:
            print("\n\n\nThere is nothing for you in that direction. Please choose a valid direction.") 
    elif choice == 'q':
        print('Farewell adventurer. Until next time.')    
    else:
        print('\n\nPlease select a valid direction, or press "q" if you would like to quit the game.')