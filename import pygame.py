import pygame
import time
import random

snake_speed = 15
window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    global score
    score = 0
    game_exit = False
    game_over_flag = False
    lead_x = window_x/2
    lead_y = window_y/2
    lead_x_change = 0
    lead_y_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, window_x - snake_speed) / 10.0) * 10.0
    foody = round(random.randrange(0, window_y - snake_speed) / 10.0) * 10.0

    while not game_exit:
        while game_over_flag == True:
            game_window.fill(black)
            game_over()
            show_score(1, white, 'times', 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over_flag = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over_flag = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -snake_speed
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = snake_speed
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -snake_speed
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = snake_speed
                    lead_x_change = 0

        if lead_x >= window_x or lead_x < 0 or lead_y >= window_y or lead_y < 0:
            game_over_flag = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        game_window.fill(black)
        pygame.draw.rect(game_window, red, [foodx, foody, snake_speed, snake_speed])
        snake_Head = []
        snake_Head.append(lead_x)
        snake_Head.append(lead_y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over_flag = True

        snake(snake_speed, snake_List)
        show_score(1, white, 'times', 20)
        pygame.display.update()

        if lead_x == foodx and lead_y == foody:
            foodx = round(random.randrange(0, window_x - snake_speed) / 10.0) * 10.0
            foody = round(random.randrange(0, window_y - snake_speed) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10

        fps.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
