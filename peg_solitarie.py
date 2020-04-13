import pygame
from pygame.locals import *
import time



UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
x1, y1 = 195, 55
x2, y2 = 265, 125

tab_positions = {(195,55): True, 
                 (265,55): True, 
                 (335,55): True,
                 (195,125): True, 
                 (265,125): True, 
                 (335,125): True,
                 (55,195): True, 
                 (125,195): True, 
                 (195,195): True, 
                 (265,195): True, 
                 (335,195): True, 
                 (405,195): True, 
                 (475,195): True, 
                 (55,265): True, 
                 (125,265): True, 
                 (195,265): True, 
                 (265,265): False, 
                 (335,265): True, 
                 (405,265): True, 
                 (475,265): True, 
                 (55,335): True, 
                 (125,335): True, 
                 (195,335): True, 
                 (265,335): True, 
                 (335,335): True, 
                 (405,335): True, 
                 (475,335): True, 
                 (195,405): True, 
                 (265,405): True, 
                 (335,405): True,
                 (195,475): True, 
                 (265,475): True, 
                 (335,475): True,
                }

invalid_moves = ((125,55), (125,125), (55,125),
                 (405,55), (405,125), (475,125),
                 (55,405), (125,405), (125,475),
                 (405,405), (475,405), (405,475),
                 (-15,195), (-15,265), (-15,335),
                 (195,-15), (265,-15), (335,-15),
                 (545,195), (545,265), (545,335),
                 (195,545), (265,545), (335,545)
                )

pygame.init()
screen = pygame.display.set_mode((600, 600))


def cursor_moves(direction):
    global x1, y1, x2, y2

    # check the cursor movement direction
    if direction == UP:
        y1 -= 70
        y2 -= 70
        if (x1, y1) in invalid_moves:  # if the new strating point is a invalid move, return to the initial point
            y1 += 70
            y2 += 70

    elif direction == DOWN:
        y1 += 70
        y2 += 70
        if (x1, y1) in invalid_moves:  # if the new strating point is a invalid move, return to the initial point
            y1 -= 70
            y2 -= 70

    elif direction == LEFT:
        x1 -= 70
        x2 -= 70
        if (x1, y1) in invalid_moves:  # if the new strating point is a invalid move, return to the initial point
            x1 += 70
            x2 += 70

    elif direction == RIGHT:
        x1 += 70
        x2 += 70
        if (x1, y1) in invalid_moves:  # if the new strating point is a invalid move, return to the initial point
            x1 -= 70
            x2 -= 70

    return [(x1,y1), (x1,y2), (x2,y2), (x2,y1)]
        

def draw_game_board(bg_img, piece, b_square):
    screen.blit(bg_img, (0,0))

    pygame.draw.rect(screen, (77, 26, 0), [(55, 55), (490,490)])

    for pos, is_piece in tab_positions.items():  # plot pieces int the board
        if is_piece:
            screen.blit(piece, pos)
        else:
            screen.blit(b_square, pos)

    for x in range(55, 546, 70):  # draws horizontal lines
        pygame.draw.line(screen, (20, 20, 20), (x, 55), (x, 545), 2)
    
    for y in range(55, 546, 70):  # draws horizontal lines
        pygame.draw.line(screen, (20, 20, 20), (55, y), (545, y), 2)

    pygame.draw.line(screen, (97, 51, 24), (55, 55), (55, 545), 4)
    pygame.draw.line(screen, (97, 51, 24), (55, 55), (545, 55), 4)
    pygame.draw.line(screen, (97, 51, 24), (545, 55), (545, 545), 4)
    pygame.draw.line(screen, (97, 51, 24), (55, 545), (545, 545), 4)


def set_cursor(key_pressed, direction):
    # set the new cursor position 
    if key_pressed:
        cursor = cursor_moves(direction)
    else:
        cursor = [(x1,y1), (x1,y2), (x2,y2), (x2,y1)]
    
    return cursor


def select_available_movements(curosr_at):
    green_b_square = pygame.Surface((70,70))
    green_b_square.fill((153, 255, 102))

    move_sum = 140  # value to sum to get in the available positions
    next_piece_sum = 70  # value to sum to get in the piece next to the current piece

    sum_types = {'up': [(curosr_at[0], (curosr_at[1] - move_sum)), (curosr_at[0], (curosr_at[1] - next_piece_sum))],
                 'down': [(curosr_at[0], (curosr_at[1] + move_sum)), (curosr_at[0], (curosr_at[1] + next_piece_sum))],
                 'left': [((curosr_at[0] - move_sum), curosr_at[1]), ((curosr_at[0] - next_piece_sum), curosr_at[1])],
                 'right': [((curosr_at[0] + move_sum), curosr_at[1]), ((curosr_at[0] + next_piece_sum), curosr_at[1])]
                }

    # list of values that mark the available position(s) to move in
    to_paint = [v[0] for v in list(sum_types.values()) if v[0] in list(tab_positions) and tab_positions[v[1]]]

    if to_paint:
        for i in to_paint:
            if not tab_positions[i]:  # plot a green square in the available position(s)
                screen.blit(green_b_square, i)
                pygame.draw.lines(screen, (102, 255, 26), True, [(i[0], i[1]), (i[0], i[1]+70), (i[0]+70, i[1]+70), (i[0]+70, i[1])], 3)
    
    return to_paint


def move_piece(piece, possible_moves, cursor, piece_position):
    global tab_positions
    if cursor[0] in possible_moves:  # check if the cursor is in a available location for the piece to move
        # Removes the piece between the cursor and the current-piece's position (capture)
        if cursor[0][0] > piece_position[0][0]:
            tab_positions[(piece_position[0][0]+70, piece_position[0][1])] = False
        elif cursor[0][0] < piece_position[0][0]:
            tab_positions[(piece_position[0][0]-70, piece_position[0][1])] = False
        elif cursor[0][1] > piece_position[0][1]:
            tab_positions[(piece_position[0][0], piece_position[0][1]+70)] = False
        elif cursor[0][1] < piece_position[0][1]:
            tab_positions[(piece_position[0][0], piece_position[0][1]-70)] = False
        
        tab_positions[piece_position[0]] = False  # removes the piece from its current position
        
        tab_positions[cursor[0]] = True  # places the piece in the cursor's position
        

def check_game_s_end(possible_moves):
    if possible_moves:
        return False
    else:
        rem = [k for k, v in list(tab_positions.items()) if v]  # Gets the remainig pieces' positions in the board

    # Method to catch linear game over is not working
    if len(rem) == 1:
        return 'Victory'
    else:
        end_game = True
        for i in range(0, len(rem)):
            for j in range(i+1, len(rem)):
                if rem[i][0] > rem[j][0] and rem[i][1] == rem[j][1]:
                    if not tab_positions.get((rem[i][0]+70, rem[i][1])) or not tab_positions.get((rem[j][0]-70, rem[j][1])):
                        if rem[i][0] - rem[j][0] == 70:
                            end_game = False
                            break

                elif rem[i][0] < rem[j][0] and rem[i][1] == rem[j][1]:
                    if not tab_positions.get((rem[i][0]-70, rem[i][1])) or not tab_positions.get((rem[j][0]+70, rem[j][1])):
                        if rem[j][0] - rem[i][0] == 70:
                            end_game = False
                            break
                
                elif rem[i][0] == rem[j][0] and rem[i][1] > rem[j][1]:
                    if not tab_positions.get((rem[i][0], rem[i][1]+70)) or not tab_positions.get((rem[j][0], rem[j][1]-70)):
                        if rem[i][1] - rem[j][1] == 70:
                            end_game = False
                            break

                elif rem[i][0] == rem[j][0] and rem[i][1] < rem[j][1]:
                    if not tab_positions.get((rem[i][0], rem[i][1]-70)) or not tab_positions.get((rem[j][0], rem[j][1]+70)):
                        if rem[j][1] - rem[i][1] == 70:
                            end_game = False
                            break
        if end_game:
            return 'end_game'




pygame.display.set_caption("Peg-Solitarie")
std_font = pygame.font.SysFont('consolas', 25)
std_b_font = pygame.font.SysFont('consolas', 25, bold=True)
clock = pygame.time.Clock()

# telas = {'menu': desenha_menu(),
#          'jogo': desenha_jogo()
#         }


def montar_jogo():
    global tab_positions

    white_b_square = pygame.Surface((70,70))
    white_b_square.fill((221, 193, 136))

    piece = pygame.image.load('c:/users/user/documents/python/hunter-sDungeon/game_piece.png').convert()
    bg = pygame.image.load('c:/users/user/documents/python/hunter-sDungeon/beech-red.jpg').convert()
    
    global x1, y1, x2, y2
    cursor_pos = [x1, y1, x2, y2]
    cursor_direction = UP
    cursor_select = False
    possible_moves = False

    while True:
        key_pressed = False
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    cursor_direction = UP
                    key_pressed = True
                elif event.key == K_DOWN:
                    cursor_direction = DOWN
                    key_pressed = True
                elif event.key == K_LEFT:
                    cursor_direction = LEFT
                    key_pressed = True
                elif event.key == K_RIGHT:
                    cursor_direction = RIGHT
                    key_pressed = True

                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    cursor_select = True
                else:
                    cursor_select = False
                
                if event.key == K_ESCAPE:
                    cursor_select = False
                

        draw_game_board(bg, piece, white_b_square)
        cursor = set_cursor(key_pressed, cursor_direction)

        if cursor_select and tab_positions[cursor[0]]:
            pygame.draw.lines(screen, (102, 255, 26), True, cursor, 3)
            possible_moves = select_available_movements(cursor[0])
            last_cursor = cursor

            if check_game_s_end(possible_moves) == False:
                pass
            elif check_game_s_end(possible_moves) == 'Victory':
                victory_screen = std_font.render('VICOTRY !!!', True, (0,0,0))
                victory_rect = victory_screen.get_rect()
                victory_rect.midtop = (600 // 2, 175)
                screen.blit(victory_screen, victory_rect)
                pygame.display.update()
                pygame.time.wait(700)
                break

            elif check_game_s_end(possible_moves) == 'end_game':
                game_over_screen = std_font.render('GAME OVER', True, (0,0,0))
                game_over_rect = game_over_screen.get_rect()
                game_over_rect.midtop = (600 // 2, 175)
                screen.blit(game_over_screen, game_over_rect)
                pygame.display.update()
                pygame.time.wait(700)
                break
                
        elif cursor_select and (not tab_positions[cursor[0]]) and possible_moves:
            move_piece(piece, possible_moves, cursor, last_cursor)
            possible_moves = False
        else:
            pygame.draw.lines(screen, (204, 41, 0), True, cursor, 3)

        pygame.display.update()
    
    desenha_menu()


def desenha_menu():
    clock.tick(10)
    my_direction = UP
    enter = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    time_wait = 10
                    my_direction = UP
                if event.key == K_DOWN:
                    time_wait = 10
                    my_direction = DOWN
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    enter = True

        
        screen.fill((0, 0, 0))    

        peg_solitarie_font = pygame.font.SysFont('consolas', 40)
        peg_solitarie_screen = peg_solitarie_font.render('Peg-Solitarie', True, (255, 255, 255))
        peg_solitarie_area = peg_solitarie_screen.get_rect()
        peg_solitarie_area.midtop = (600 // 2, 20)
        screen.blit(peg_solitarie_screen, peg_solitarie_area)

        play_font = std_font.render('Play', True, (255, 255, 255))
        play_rect = play_font.get_rect()
        play_rect.midtop = (600 // 2, 150)
        screen.blit(play_font, play_rect)

        quit_font = std_font.render('Quit', True, (255, 255, 255))
        quit_rect = quit_font.get_rect()
        quit_rect.midtop = (600 // 2, 175)
        screen.blit(quit_font, quit_rect)
        
        pygame.time.wait(250)
        pygame.display.update()

        
        if my_direction == UP:
            play_font = std_b_font.render('Play', True, (0, 255, 0))
            play_rect = play_font.get_rect()
            play_rect.midtop = (600 // 2, 150)
            screen.blit(play_font, play_rect)
            if enter:
                screen.fill((219, 202, 105))
                pygame.display.update()
                montar_jogo()
                pygame.time.wait(7000)
                break

        elif my_direction == DOWN:
            quit_font = std_b_font.render('Quit', True, (0, 255, 0))
            quit_rect = quit_font.get_rect()
            quit_rect.midtop = (600 // 2, 175)
            screen.blit(quit_font, quit_rect)
            if enter:
                pygame.quit()
                exit()

        pygame.time.wait(250)
        pygame.display.update()
    
desenha_menu()


pygame.quit()