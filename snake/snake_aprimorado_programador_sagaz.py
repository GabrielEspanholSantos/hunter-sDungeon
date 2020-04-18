import pygame, random
from pygame.locals import *
import os
dir_name = os.path.join(os.path.dirname(__file__))

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def on_grid_random():
    x = random.randint(10,580)
    y = random.randint(10,580)
    return (x//10 * 10, y//10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def alter_snake_speed(size, speed):
    if size % 8 == 0:
        speed = speed + 1
    return speed   


def set_direction(my_direction, snake):
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    return snake[0]


def make_game(best_score):
    snake = [(200, 200), (210, 200), (220,200)]

    snake_head_skin = pygame.Surface((10,10))
    snake_head_skin.fill((51, 102, 255))

    snake_body_skin = pygame.Surface((10,10))
    snake_body_skin.fill((51, 153, 255))

    apple_pos = on_grid_random()
    apple = pygame.Surface((10,10))
    apple.fill((255,0,0))

    my_direction = LEFT
    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0
    snake_speed = 10
    snake_size = len(snake)
    dead_line = False

    while True:
        clock.tick(snake_speed)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                elif event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                elif event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
                elif event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT


        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0,0))
            snake_size = len(snake)
            snake_speed = alter_snake_speed(snake_size, snake_speed)
            score += 1


        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        snake[0] = set_direction(my_direction, snake)

        if list(filter(lambda part: collision(snake[0], part), snake[1:-1])):
            dead_line = True
        
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] == 0 or snake[0][1] == 0:
            dead_line = True

        screen.fill((51, 204, 51))
        screen.blit(apple, apple_pos)

        score_font = font.render(f'Score: {score}', True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (600 - 120, 10)
        screen.blit(score_font, score_rect)

        b_score_font = font.render(f'Best-Score: {best_score}', True, (255, 255, 255))
        b_score_rect = b_score_font.get_rect()
        b_score_rect.topleft = (40, 10)
        screen.blit(b_score_font, b_score_rect)

        for i, pos in enumerate(snake):
            if i == 0:
                screen.blit(snake_head_skin,pos)
            else:
                screen.blit(snake_body_skin,pos)
        
        if dead_line:
            if score > best_score:
                with open(os.path.join(dir_name, 'best_score.txt'), 'w') as r:
                    r.write(str(score))
            break

        pygame.display.update()

    while True:
        game_over_font = pygame.font.Font('freesansbold.ttf', 50)
        game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (600 // 2, 20)
        screen.blit(game_over_screen, game_over_rect)
        pygame.display.update()
        pygame.time.wait(60)
        draw_menu()


def draw_menu():
    clock.tick(10)
    direction = UP
    enter = False
    font = pygame.font.SysFont('consolas', 30)
    i = 0
    current_play_color = (255,255,255)
    current_quit_color = (255,255,255)

    with open(os.path.join(dir_name, 'best_score.txt'), 'r') as r:
        try:
            best_score = int(r.readline())
        except:
            best_score = -1

    while True:
        if i == 3:
            i = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    direction = UP
                if event.key == K_DOWN:
                    direction = DOWN
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    enter = True
        
        screen.fill((0, 0, 0))

        font_colors = ((255, 255, 255), (204, 0, 102), (0, 255, 255))
        if direction == UP:
            current_play_color = font_colors[2]
            current_quit_color = font_colors[0]
            if enter:
                screen.fill((51, 204, 51))
                pygame.display.update()
                make_game(best_score)
                pygame.time.wait(7000)
                break

        elif direction == DOWN:
            current_play_color = font_colors[0]
            current_quit_color = font_colors[2]
            if enter:
                pygame.display.quit()
                pygame.quit()
                exit()
                
                
        snake_font = pygame.font.SysFont('consolas', 40)
        snake_font_screen = snake_font.render('Snake Game', True, font_colors[i])
        snake_font_area = snake_font_screen.get_rect()
        snake_font_area.midtop = ((600 // 2)- 5 + (i*10), 60 - (i*10))
        screen.blit(snake_font_screen, snake_font_area)

        play_font = font.render('Play', True, current_play_color)
        play_area = play_font.get_rect()
        play_area.midtop = (600 // 2, 170)
        screen.blit(play_font, play_area)

        quit_font = font.render('Quit', True, current_quit_color)
        quit_area = quit_font.get_rect()
        quit_area.midtop = (600 // 2, 200)
        screen.blit(quit_font, quit_area)


        pygame.time.wait(250)
        pygame.display.update()


        i += 1

draw_menu()

