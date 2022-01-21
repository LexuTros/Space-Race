#!/usr/bin/env python3
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
from logging import exception

# Utility Functions:
def player_coords(state):
    for y, line in enumerate(state):
        for x, char in enumerate(line):
            if char == "o":
                return y, x # =(player_y, player_x) coordinates

def possible_movement(state, player_y, player_x):
    res = ()
    if 0 <= player_y + 1 < len(state):
        if state[player_y + 1][player_x] == " ": res += ("down",)
    if 0 <= player_x - 1 < len(state[player_y]):
        if state[player_y][player_x - 1] == " ": res += ("left",)
    if 0 <= player_x + 1 < len(state[player_y]):
        if state[player_y][player_x + 1] == " ": res += ("right",)
    if 0 <= player_y - 1 < len(state):
        if state[player_y - 1][player_x] == " ": res += ("up",)
    return res # =Tuple of possible movement directions in alphabetic order



# Main Function:
def move(state, direction):

    # Check if Gamestate is valid:
    valid_state_chars = [" ", "#", "o"]
    player_counter = 0
    # Correct state type
    if not isinstance(state, tuple):
        raise Warning("The game state has the wrong Type (must be a tuple)")
    for e in state:
        if not isinstance(e, str):
            raise Warning("A line of the game state has the wrong Type (must be a string)")
    # At least 1 line
    if len(state) == 0:
        raise Warning("Game state is empty (doesn't contain any elements)")
    for line in state:
        # At least 1 char per line
        if len(line) == 0:
            raise Warning("Game state contains an empty line")
        # All lines have same lenght
        if len(line) != len(state[0]):
            raise Warning("Lines of game state have different lenghts")
        # Valid State chars
        for char in line:
            if char not in valid_state_chars:
                raise Warning("Game state contains invalid char")
        # One Player exists
        player_counter += line.count("o")
    if player_counter != 1:
        raise Warning("There are to many or no players in the game (only one player is allowed)")
    # Min one possible Movement
    player_y, player_x = player_coords(state)
    possible_moves = possible_movement(state, player_y, player_x)
    if len(possible_moves) == 0:
        raise Warning("The player can't move (is surrounded by rocks)")
    

    # Check if Move is valid:
    valid_directions = ["down", "left", "right", "up"]
    # Correct direction Type
    if not isinstance(direction, str):
        raise Warning("The direction has the wrong Type (must be a string)")
    # Valid direction
    if direction not in valid_directions:
        raise Warning("The given direction is invalid (valid directions: up, down, left, right)")
    # Direction is not obstructed
    if direction not in possible_moves:
        raise Warning("The player is obstructed (can't move in this direction)")
    

    # Execute valid Move (edit state):
    emp = ""
    # List() the state
    listed_state = list(state)
    for index, element in enumerate(listed_state): 
        listed_state[index] = list(element)
    # Edit the state
    listed_state[player_y][player_x] = " "
    if direction == "right": listed_state[player_y][player_x + 1] = "o"
    if direction == "left": listed_state[player_y][player_x - 1] = "o"
    if direction == "down": listed_state[player_y + 1][player_x] = "o"
    if direction == "up": listed_state[player_y - 1][player_x] = "o"
    # Turn state back into tuple of strings
    for index, element in enumerate(listed_state):
        listed_state[index] = emp.join(element)
    new_state = tuple(listed_state)

    # Find new possible Moves:
    player_y_new, player_x_new = player_coords(new_state)
    possible_moves_new = possible_movement(new_state, player_y_new, player_x_new)


    return new_state, possible_moves_new


# Uni version:
# The following line calls the function and prints the return
# value to the Console.

# s1 = (
#     "#####   ",
#     "###    #",
#     "#   o ##",
#     "   #####"
# )
# s2 = move(s1, "right")

# print("= New State =")
# print("\n".join(s2[0]))
# print("\nPossible Moves: {}".format(s2[1]))







# Interactive Mode :)
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
)
y1, x1 = player_coords(s1)
# First output
print("\n".join(s1))
print("Possible Moves: " + str(possible_movement(s1, y1, x1)))
d1 = input()
# Interactive While loop
while d1 != "stop":
    s2 = move(s1, d1)
    print("= New State =")
    print("\n".join(s2[0]))
    print("Possible Moves: {}".format(s2[1]))
    s1 = s2[0]
    d1 = input()
    while d1 not in s2[1] and d1 != "stop":
        print("\n".join(s2[0]))
        print(f"This move is not possible, Possible Moves are: {s2[1]}")
        d1 = input()
