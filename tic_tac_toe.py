# Import termcolor so I can experiment with colors.
from termcolor import colored
# Make a template for my Tic Tac Toe.
mapping = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]


# Define update function that will store the players progress.
def update():
    win_combination = [[[mapping[0][0]], [mapping[0][1]], [mapping[0][2]]],
                       [[mapping[1][0]], [mapping[1][1]], [mapping[1][2]]],
                       [[mapping[2][0]], [mapping[2][1]], [mapping[2][2]]],
                       [[mapping[0][0]], [mapping[1][0]], [mapping[2][0]]],
                       [[mapping[0][1]], [mapping[1][1]], [mapping[2][1]]],
                       [[mapping[0][2]], [mapping[1][2]], [mapping[2][2]]],
                       [[mapping[0][0]], [mapping[1][1]], [mapping[2][2]]],
                       [[mapping[2][0]], [mapping[1][1]], [mapping[0][2]]]]
    # Return data progress.
    return win_combination


# Make a list for used moves.
used_moves = []


# Make a function to display the progress for the players
# whenever I need it.
def display_progress():
    q = colored("Q", "blue")
    w = colored("W", "blue")
    e = colored("E", "blue")
    print(colored("    1   2   3", "blue"))
    print("  ╔═══╦═══╦═══╗")
    print(f"{q} ║ {mapping[0][0]} ║ {mapping[0][1]} ║ {mapping[0][2]} ║")
    print("  ╠═══╬═══╬═══╣")
    print(f"{w} ║ {mapping[1][0]} ║ {mapping[1][1]} ║ {mapping[1][2]} ║")
    print("  ╠═══╬═══╬═══╣")
    print(f"{e} ║ {mapping[2][0]} ║ {mapping[2][1]} ║ {mapping[2][2]} ║")
    print("  ╚═══╩═══╩═══╝")


# Call display progress to let the players decide first.
display_progress()


# Create a class where every player has the same attributes instance variable and methods
# but different output depends later on on my @staticmethod.
class Player:
    # __init__ initialise player's name and symbol.
    def __init__(self, name="Unknown", symbol="Unknown"):
        self.name = name
        self.symbol = symbol
    # I need to define a getter and a setter for each instance.
    # @property so I can refer to the function or even better to get the return variable
    # without calling the function just mentioning their (object.name).
    @property
    def name(self):
        return self.__name
    # @setter so I can protect the instance variable from bad value assignment
    # and not pass it to the getter if it is not the needed data.
    @name.setter
    def name(self, name):
        if name.isalpha():
            self.__name = name
    # I need to define a getter and a setter for each instance.
    # @property so I can refer to the function or even better to get the return variable
    # without calling the function just mentioning their (object.name).
    @property
    def symbol(self):
        return self.__symbol
    # @setter so I can protect the instance variable from bad value assignment
    # and not pass it to the getter if it is not the needed data.
    @symbol.setter
    def symbol(self, symbol):
        if symbol in ["X", "O"]:
            self.__symbol = symbol


# Make a class Game
# I call this a utility class because to be honest it has
# nothing to do with the Super class if I inherited it.
class Game:
    # Create a method called start that starts the game
    # and altering players whenever it is called.
    def start(self, player_one, player_two):
        # Round counter.
        round_count = 0
        # While loop to switch between players.
        while round_count <= 4:
            # If statements.
            # Condition Tie.
            if round_count == 4:
                print("============> TIE")
                break
            # Increment round_count by 1.
            round_count += 1
            # Condition player 1 has won.
            # Game over means end the game.
            if self.round(player_one) == "Game Over":
                # Output the results.
                print("{} has won".format(player_one.name))
                break
            # Condition player 2 has won.
            # Game over means end the game.
            if self.round(player_two) == "Game Over":
                # Output the results.
                print("{} has won".format(player_two.name))
                break
    # Make a static method because this method does not need any self or
    # any instance variable.
    # This method will only do logic.
    @staticmethod
    def round(players):
        print("This is {}'s turn".format(colored(players.name, "blue")))
        while True:
            # Prompt the players to input their next move.
            move = input("Enter your next move: ")
            if move in used_moves:
                # Used move display error.
                print("Sorry! but this move has already been used.")
            else:
                # Add new move to used_moves.
                used_moves.append(move)
                break

        # Initiating logic.
        column = int(move[0]) - 1
        row = move[1].upper()
        row_num = None
        if row == "Q":
            row_num = 0
        elif row == "W":
            row_num = 1
        elif row == "E":
            row_num = 2
        # Some styling.
        if players.symbol == "X":
            mapping[row_num][column] = colored(players.symbol, "red")
        elif players.symbol == "O":
            mapping[row_num][column] = colored(players.symbol, "green")
        # Update progress.
        update()
        # Display progress.
        display_progress()
        # Check my win condition logic.
        for i in update():
            if i[0] == i[1] == i[2]:
                # Return game over if one of the players has won.
                return "Game Over"


# Make a function to declare position in the game.
def define_your_position():
    # Prompt the players to enter their name.
    while True:
        player_1 = input("Enter your name (Player 1): ")
        if player_1.isalpha():
            break
        else:
            print("Sorry, name can only be letters.")

    # Prompt the players to enter their symbol.
    while True:
        player_1_sym = input("{} pick X or O: ".format(player_1))
        if player_1_sym in ["X", "x", "O", "o"]:
            break
        else:
            print("Make sure you enter X or O.")
    # Second player name.
    while True:
        player_2 = input("Enter your name (Player 2): ")
        if player_2.isalpha():
            break
        else:
            print("Sorry, name can only be letters.")
    player_2_sym = None
    # Symbol is chosen by process of elimination.
    if player_1_sym.upper() == "X":
        player_2_sym = "O"
    elif player_1_sym.upper() == "O":
        player_2_sym = "X"
    # Return 4 variables to unpack.
    return player_1, player_1_sym.upper(), player_2, player_2_sym


# Setting up players object.
p1_name, p1_sym, p2_name, p2_sym = define_your_position()
player_one = Player(p1_name, p1_sym)
player_two = Player(p2_name, p2_sym)
# Start the game and pass players.
Game().start(player_one, player_two)