import getpass
import random
import time

colours = ["b", "r", "w", "bl", "y", "g"]

def read_input():
    user_input = []
    data = input("Enter the colors with ',' between each:\n")
    user_input = data.split(',')
    return user_input

def read_hidden_combination():
    input_data = []
    # getpass will hide user input, adds some secrecy
    data = getpass.getpass("Enter the colour combination with , as seperator: ")
    input_data = data.split(',')
    return input_data

def generate_response(game_board, input_board):
    temp_game_board = game_board.copy()
    temp_input_board = input_board.copy()
    response = []
    i = 0
    while(i < len(temp_game_board)):
        if(temp_game_board[i] == temp_input_board[i]):
            response.append('R')
            # remove the matched colours from both boards for next step
            temp_game_board.pop(i)
            temp_input_board.pop(i)
        else:
            i += 1
    # if response is already full, then no need to check for any correct colours
    if(len(response) == 4):
        return response

    for j in range(len(temp_game_board)):
        if(temp_game_board[j] in temp_input_board):
            response.append('W') # W - correct colour but incorrect position
    return response

class masterMind():

    def __init__(self):
        self.game_board = []
        self.game_turn = 0
        self.input_boards = []
        self.response_boards = []

    def generate_board(self):
        seed = int(time.time())
        random.seed(seed)
        game_board = []
        for i in range(4):
            random_index = random.randint(0, len(colours)-1)
            game_board.append(colours[random_index])
        self.game_board = game_board

    # boolean function that prints the appropiate messages before returning
    def game_over(self):
        if(len(self.input_boards) == 0 or len(self.response_boards) == 0): # no input/responses yet
            return False
        if(self.game_turn >= 10):
            print("Game Over!")
            return True
        elif(self.response_boards[len(self.response_boards)-1] == ['R', 'R', 'R', 'R']):
            print("Won in " + str(self.game_turn) + " turns!")
            return True
        else:
            return False

    # print the boards at current state
    def print_game_state(self):
        for i in range(len(self.input_boards)):
            print(self.input_boards[i], end = " ")
            print(self.response_boards[i])

    def start(self):

        choice = input("Please select 1 - user input colour combination or 2 - random colour combination: ")

        if(int(choice) == 2):
            self.generate_board()
        elif(int(choice) == 1):
            game_board = read_hidden_combination()
            self.game_board = game_board
        else:
            print("Unknown input, exit")
            return

        while(not self.game_over()):
            self.game_turn += 1 # progress a game turn
            print("Turn " + str(self.game_turn))
            input_data = read_input()
            self.input_boards.append(input_data) # add input board to boards to print later

            current_response = generate_response(self.game_board, input_data)
            self.response_boards.append(current_response)
            self.print_game_state()
