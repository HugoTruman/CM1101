#!/usr/bin/python3

from map import rooms
import string

def remove_punct(text):
    output=""
    for s in text():
        if s not in string.punctuation:
            output+=s
    return output


    
def remove_spaces(text):
    return text.replace(" ", "")

def normalise_input(user_input):
    return remove_spaces(remove_punct(user_input.lower))

    
def display_room(room):
    print room["name"], "\n", room["description"].upper()

    
def exit_leads_to(exits, direction):
    #where the direction leads to
    return rooms[exits[direction]]
    

def print_menu_line(direction, leads_to):
    print ("Go " + direction + " to " + leads_to)


def print_menu(exits):

    print("You can:")
    for key in exits:
        print_menu_line(key, exits[key])

    print("Where do you want to go?")


def is_valid_exit(exits, user_input):

    return user_input in exits

def menu(exits):
    # Repeat until the player enter a valid choice
    while True:
        # COMPLETE THIS PART:
        
        # Display menu
        print_menu(exits)

        user_input=raw_input("> ")
        user_input= normalise_input(user_input)

        if is_valid_exit(exits,user_input):
            return user_input
        else:
            print user_input, "is not valid. You are playing the game wrong. Say something else"
       # display_room(move(exits,is_valid))



        # Normalise the input

        # Check if the input makes sense (is valid exit)
        #is_valid_exit()
            # If so, return the player's choice

def move(exits, direction):
    #look to see if it should return true of false
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    # Start game at the reception
    current_room = rooms["Reception"]
    # Main game loop
    while True:
        # Display game status (room description etc.)
        display_room(current_room)

        # What are the possible exits from the current room?
        exits = current_room["exits"]

        # Show the menu with exits and ask the player
        direction = menu(exits)

        # Move the protagonist, i.e. update the current room
        current_room = move(exits, direction)

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
if __name__ == "__main__":
    main()