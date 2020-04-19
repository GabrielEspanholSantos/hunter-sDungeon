import os
import time
tabs = '\t\t\t\t\t'

x = 'X'
o = 'O'

def clear():
    os.system('cls')
    

def create_board():
    board = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
    
    return board


def print_board(board):
    print(tabs+' '+board['7']+' | '+board['8']+' | '+board['9']+' ')
    print(tabs+'-----------')
    print(tabs+' '+board['4']+' | '+board['5']+' | '+board['6']+' ')
    print(tabs+'-----------')
    print(tabs+' '+board['1']+' | '+board['2']+' | '+board['3']+' ')


def alter_board(board, pos, symbol):
    if is_possible_move(board, pos):
        board[pos] = symbol
        return True, board
    else:
        return False, board


def is_possible_move(board, pos):
    return board[pos] == ' '


def check_victory(board, piece):
    victory = False
    draw = True
    
    for i in range(1,5):
        for k in board.keys():
            if board[k] == ' ':
                draw = False

            if i == 1 and int(k) in [1,4,7]:
                pos1 = int(k)
            elif i == 2 and int(k) == 3:
                pos1 = int(k)
            elif i == 3 and int(k) in [1,2,3]:
                pos1 = int(k)
            elif i == 4 and int(k) == 1:
                pos1 = int(k)
            else:
                continue

            pos2 = str(pos1+i)
            pos3 = str(pos1+(2*i))
            pos1 = str(pos1)

            if board[pos1] == piece and board[pos2] == piece and board[pos3] == piece:
                victory = True
                break
    
    return (draw, victory)


def make_move(board, symbol, next_move):
    moved, board = alter_board(board, next_move, symbol)
    draw, victory = check_victory(board, symbol)

    return moved, board, draw, victory


def play_again():
    init = init_game()
    return init

        
def init_game():
    clear()
    board = create_board()
    player1_type = input("Player 1, do you want to be X or O? ").upper()

    if player1_type == x:
        player1_turn = True
        p1_symbol = x
        p2_symbol = o
        print('Player 1, you will go first\n')
    elif player1_type == o:
        player1_turn = False
        p1_symbol = o
        p2_symbol = x
        print('Player 2, you will go first\n')
    else:
        print("Invalid symbol, please, type again.\n")
        time.sleep(1)
        return 'y'
    
    while True:
        print_board(board)

        print("It's player1's turn\n") if player1_turn else print("It's player2's turn\n")
        next_move = input('Choose your next position [1-9]: ')
        if next_move.isnumeric():
            if int(next_move) > 0 and int(next_move) < 10:
                if player1_turn:
                    moved, board, draw, victory = make_move(board, p1_symbol, next_move)
                    
                    if draw:
                        clear()
                        print_board(board)
                        print("It's a DRAW!")
                        break
                    elif victory:
                        clear()
                        print_board(board)
                        print("Congrats, player 1, you won the game.")
                        break

                    if moved:
                        player1_turn = False
                        clear()
                    else:
                        clear()
                        print('This is not a valid movement, please type again\n')
                        continue
                else:
                    moved, board, draw, victory = make_move(board, p2_symbol, next_move)

                    if draw:
                        clear()
                        print_board(board)
                        print("It's a DRAW!")
                        break
                    elif victory:
                        clear()
                        print_board(board)
                        print("Congrats, player 2, you won the game.")
                        break

                    if moved:
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
        else:
            clear()
            print('Wrong input, please, type again.\n')
            continue
    
    ans = input("Do you want to play again? [y | n] ").lower()
    return ans

init = 'y'
while init == 'y':
    init = play_again()


        