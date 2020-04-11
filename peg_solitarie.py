import pygame
from pygame.locals import *
import time



UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
x1, y1 = 195, 55
x2, y2 = 265, 125

tab_positions = {0: [(195,55),True], 
                         1: [(265,55),True], 
                         2: [(335,55),True],
                         3: [(195,125),True], 
                         4: [(265,125), True], 
                         5: [(335,125), True],
                         6: [(55,195), True], 
                         7: [(125,195), True], 
                         8: [(195,195), True], 
                         9: [(265,195), True], 
                         10: [(335,195), True], 
                         11: [(405,195), True], 
                         12: [(475,195), True], 
                         13: [(55,265), True], 
                         14: [(125,265), True], 
                         15: [(195,265), True], 
                         16: [(265,265), False], 
                         17: [(335,265), True], 
                         18: [(405,265), True], 
                         19: [(475,265), True], 
                         20: [(55,335), True], 
                         21: [(125,335), True], 
                         22: [(195,335), True], 
                         23: [(265,335), True], 
                         24: [(335,335), True], 
                         25: [(405,335), True], 
                         26: [(475,335), True], 
                         27: [(195,405), True], 
                         28: [(265,405), True], 
                         29: [(335,405), True],
                         30: [(195,475), True], 
                         31: [(265,475), True], 
                         32: [(335,475), True],
                        }

pygame.init()
screen = pygame.display.set_mode((600, 600))


def cursor_moves(direction):
    global x1, y1, x2, y2
    invalid_moves = ((125,55), (125,125), (55,125),
                     (405,55), (405,125), (475,125),
                     (55,405), (125,405), (125,475),
                     (405,405), (475,405), (405,475),
                     (-15,195), (-15,265), (-15,335),
                     (195,-15), (265,-15), (335,-15),
                     (545,195), (545,265), (545,335),
                     (195,545), (265,545), (335,545)
                     )

    if direction == UP:
        y1 -= 70
        y2 -= 70
        if (x1, y1) in invalid_moves:
            y1 += 70
            y2 += 70

    elif direction == DOWN:
        y1 += 70
        y2 += 70
        if (x1, y1) in invalid_moves:
            y1 -= 70
            y2 -= 70

    elif direction == LEFT:
        x1 -= 70
        x2 -= 70
        if (x1, y1) in invalid_moves:
            x1 += 70
            x2 += 70

    elif direction == RIGHT:
        x1 += 70
        x2 += 70
        if (x1, y1) in invalid_moves:
            x1 -= 70
            x2 -= 70

    return [(x1,y1), (x1,y2), (x2,y2), (x2,y1)]
        

def draw_board(bg_img, piece, b_square):
    screen.blit(bg_img, (0,0))

    pygame.draw.rect(screen, (77, 26, 0), [(55, 55), (490,490)])

    for pos, is_piece in tab_positions.values():
        if is_piece:
            screen.blit(piece, pos)
        else:
            screen.blit(b_square, pos)

    for x in range(55, 546, 70):
        pygame.draw.line(screen, (20, 20, 20), (x, 55), (x, 545), 2)
    
    for y in range(55, 546, 70):
        pygame.draw.line(screen, (20, 20, 20), (55, y), (545, y), 2)

    pygame.draw.line(screen, (97, 51, 24), (55, 55), (55, 545), 4)
    pygame.draw.line(screen, (97, 51, 24), (55, 55), (545, 55), 4)
    pygame.draw.line(screen, (97, 51, 24), (545, 55), (545, 545), 4)
    pygame.draw.line(screen, (97, 51, 24), (55, 545), (545, 545), 4)


def set_cursor(key_pressed, direction):
    if key_pressed:
        cursor = cursor_moves(direction)
    else:
        cursor = [(x1,y1), (x1,y2), (x2,y2), (x2,y1)]
    
    return cursor


def select_available_movements():
    



pygame.display.set_caption("Peg-Solitarie")
std_font = pygame.font.SysFont('consolas', 25)
std_b_font = pygame.font.SysFont('consolas', 25, bold=True)
clock = pygame.time.Clock()

# telas = {'menu': desenha_menu(),
#          'jogo': desenha_jogo()
#         }


def montar_jogo():
    white_b_square = pygame.Surface((70,70))
    white_b_square.fill((221, 193, 136))

    piece = pygame.image.load('c:/users/user/documents/python/hunter-sDungeon/game_piece.png').convert()
    bg = pygame.image.load('c:/users/user/documents/python/hunter-sDungeon/beech-red.jpg').convert()
    
    global x1, y1, x2, y2
    cursor_pos = [x1, y1, x2, y2]
    cursor_direction = UP

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
                elif event.key == K_RETURN or event.key == K_KP_ENTER:
                    cursor_select = True

        draw_board(bg, piece, white_b_square)

        pygame.draw.lines(screen, (204, 41, 0), True, set_cursor(key_pressed, cursor_direction), 3)

        pygame.display.update()
    
   


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