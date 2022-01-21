class GameRunner:
    
    def __init__(self, state):
        self.state = state
        self.game_state_checker(state)
    
    # Utility Functions:
    def player_coords(self, state):
        for y, line in enumerate(state):
            for x, char in enumerate(line):
                if char == "o":
                    return y, x # =(player_y, player_x) coordinates

    def possible_movement(self, state, player_y, player_x):
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


    def game_state_checker(self, state):
        # Check if Gamestate is valid:
        valid_state_chars = [" ", "#", "o"]
        player_counter = 0
        # Correct state type
        if not isinstance(state, list):
            raise Warning("The game state has the wrong Type (must be a list)")
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
        # Safe current coords and possible moves
        self.player_y, self.player_x = self.player_coords(state)
        self.possible_moves = self.possible_movement(state, self.player_y, self.player_x)
        # Min one possible Movement
        if len(self.possible_moves) == 0:
            raise Warning("The player can't move (is surrounded by rocks)")
    
    
    def move_checker(self, direction):
        # Check if Move is valid:
        valid_directions = ["down", "left", "right", "up"]
        # Correct direction Type
        if not isinstance(direction, str):
            raise Warning("The direction has the wrong Type (must be a string)")
        # Valid direction
        if direction not in valid_directions:
            raise Warning("The given direction is invalid (valid directions: up, down, left, right)")
        # Direction is not obstructed
        if direction not in self.possible_moves:
            raise Warning("The player is obstructed (can't move in this direction)")
    

    def move(self, state, direction):
        emp = ""
        # List() the state
        for index, element in enumerate(state): 
            state[index] = list(element)
        # Edit the state
        state[self.player_y][self.player_x] = " "
        if direction == "right": state[self.player_y][self.player_x + 1] = "o"
        if direction == "left": state[self.player_y][self.player_x - 1] = "o"
        if direction == "down": state[self.player_y + 1][self.player_x] = "o"
        if direction == "up": state[self.player_y - 1][self.player_x] = "o"
        # Turn state back into list of strings
        for index, element in enumerate(state):
            state[index] = emp.join(element)
        self.state = state
        # Check if new state is valid
        self.game_state_checker(state)


    def runner(self, state):
        y1, x1 = self.player_coords(state)
        # First output
        print("\n".join(state))
        print("Possible Moves: " + str(self.possible_movement(state, y1, x1)))
        direction = input()
        # Interactive While loop
        while direction != "stop":
            self.move(state, direction)
            print("= New State =")
            print("\n".join(self.state))
            print("Possible Moves: {}".format(self.possible_moves))
            direction = input()
            while direction not in self.possible_moves and direction != "stop":
                print("\n".join(self.state))
                print(f"This move is not possible, Possible Moves are: {self.possible_moves}")
                direction = input()
            
                
                
if __name__ == '__main__':
    s1 = [
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
    ]
    
    game = GameRunner(s1)
    game.runner(s1)
    