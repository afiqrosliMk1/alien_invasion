import pygame

import sys

pygame.init()

speed = 1.5
scale = 2

screen = pygame.display.set_mode((240, 240))

rocket = pygame.image.load("images/00.png")
rocket = pygame.transform.scale(rocket, (rocket.get_width() * scale, rocket.get_height() * scale))
rocket_rect = rocket.get_rect()
clock = pygame.time.Clock()

moving_right_flag = False
moving_left_flag = False
moving_up_flag = False
moving_down_flag = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exiting")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left_flag = True
            elif event.key == pygame.K_RIGHT:
                moving_right_flag = True
            elif event.key == pygame.K_UP:
                moving_up_flag = True
            elif event.key == pygame.K_DOWN:
                moving_down_flag = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left_flag = False
            elif event.key == pygame.K_RIGHT:
                moving_right_flag = False
            elif event.key == pygame.K_UP:
                moving_up_flag = False
            elif event.key == pygame.K_DOWN:
                moving_down_flag = False 

    if moving_left_flag == True:
        if rocket_rect.left > 0:
            rocket_rect.x -= 1 + speed
    if moving_right_flag == True:
        if rocket_rect.right < screen.get_width():
            rocket_rect.x += 1 + speed
    if moving_up_flag == True:
        if rocket_rect.top > 0:
            rocket_rect.y -= 1 + speed
    if moving_down_flag == True:
        if rocket_rect.bottom < screen.get_height():
            rocket_rect.y += 1 + speed
    
    screen.fill((0, 0, 0))
    screen.blit(rocket, rocket_rect)
    pygame.display.flip()
    clock.tick(60)