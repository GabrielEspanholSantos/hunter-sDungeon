import os
import time

#Global Variables
tabs = '\t\t\t\t\t'
x = 'X'
o = 'O'

def clear():
    """ Clears the screen (windows only), for linux, replace 'cls' with 'clear' """
    os.system('cls')
    

def create_board():
    """ Create a board from a list, ignoring the first list position """
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return board


def print_board(board):
    """ Prints the board on the screen """

    print(tabs+' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print(tabs+'-----------')
    print(tabs+' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print(tabs+'-----------')
    print(tabs+' '+board[1]+' | '+board[2]+' | '+board[3]+' ')


def alter_board(board, pos, symbol):
    """ Places a mark on the specified position, if this position is a blank space """

    if is_possible_move(board, pos):
        board[pos] = symbol
        return True, board
    else:
        return False, board


def is_possible_move(board, pos):
    """ Checks if the specified position is a blank space """
    return board[pos] == ' '


def check_end(board, piece):
    """ Checks if the game has ended (victory or tie) """

    victory = False
    tie = True
    
    if ' ' in board:
        tie = False  # if there's a blank space it's not a tie

    for i in range(1,5):  # loop over the 4 possible intervals between victory positions
        for k in range(1,8):  # loop over the board's positions

            if ((i == 1 and k in [1,4,7]) or (i == 2 and k == 3) or 
                (i == 3 and k in [1,2,3]) or (i == 4 and k == 1)):
                pos1 = k  # initializes the starting position to make the comparisons
                pos2 = pos1+i
                pos3 = pos2+i
            else:
                continue

            if board[pos1] == board[pos2] == board[pos3] == piece:
                victory = True  # If there's a 3 pieces sequence, it's a victory
                break
    
    return (tie, victory)


def make_move(board, symbol, next_move):
    """ Calls the functions responsible for making a move """

    moved, board = alter_board(board, next_move, symbol)
    tie, victory = check_end(board, symbol)

    return moved, board, tie, victory


def choose_first():
    """ Randomly sets the first player """

    import random
    first = random.randint(0,1)

    if first == 0:
        return 'Player 1', True
    else:
        return 'Player 2', False


def play_again():
    """ If the players want to replay the game, it restarts """

    init = init_game()
    return init

        
def init_game():
    clear()
    board = create_board()
    player1_type = input("Player 1, do you want to be X or O? ").upper()  # asks the player1's piece

    # sets the players pieces
    if player1_type == x:
        p1_symbol = x
        p2_symbol = o
    elif player1_type == o:
        p1_symbol = o
        p2_symbol = x
    else:
        print("Invalid symbol, please, type again.\n")
        time.sleep(1)
        return 'y'

    # sets who goes first
    first, player1_turn = choose_first()
    print(f'{first}, you will go first\n')
    
    while True:
        print_board(board)

        # indicates whose turn is it
        print("It's player1's turn\n") if player1_turn else print("It's player2's turn\n")

        # checks if the input is valid
        try:
            next_move = int(input('Choose your next position [1-9]: '))  # asks the player's next move
        except ValueError:
            clear()
            print('Wrong input, please, type again.\n')
            continue

        if next_move > 0 and next_move < 10:  # checks if the input is between 1 and 9
            if player1_turn:
                moved, board, tie, victory = make_move(board, p1_symbol, next_move)
                
                if tie:  # if the game is tied, ends the game
                    clear()
                    print_board(board)
                    print("It's a TIE!")
                    break
                elif victory:  # if player 1 has won, ends the game
                    clear()
                    print_board(board)
                    print("Congrats, player 1, you won the game.")
                    break

                if moved:  # If player 1 played, set the turn for player 2
                    player1_turn = False
                    clear()
                else:
                    clear()
                    print('This is not a valid movement, please type again\n')
                    continue
            else:
                moved, board, tie, victory = make_move(board, p2_symbol, next_move)

                if tie:  # if the game is tied, ends the game
                    clear()
                    print_board(board)
                    print("It's a TIE!")
                    break
                elif victory:  # if player 2 has won, ends the game
                    clear()
                    print_board(board)
                    print("Congrats, player 2, you won the game.")
                    break

                if moved:  # If player 2 played, set the turn for player 2
                    player1_turn = True
                    clear()
                else:
                    clear()
                    print('This is not a valid movement, please type again\n')
                    continue                     
        else:
            clear()
            print('Your input must be between 1 and 9.\n')
            continue
            
    # checks if the players want to play again
    ans = input("Do you want to play again? [y | n] ").lower()
    return ans


cont = 5
init = 'y'

clear()
print(tabs+"WELCOME TO THE TIC-TAC-TOE GAME!")
time.sleep(3)
clear()

print(tabs+"This is a numpad based game, wich means that:\n"+tabs+"\
the positions on the board are the same as on the numeric-keypad's\n"+tabs+"\
numbers. The game will start on:")

time.sleep(10)
while cont > 0:
    print(tabs,cont)
    time.sleep(1)
    cont -= 1

while init == 'y':  # while play again returns 'y', keep restarting the game
    init = play_again()


        