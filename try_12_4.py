# import pygame

# import sys

# pygame.init()

# speed = 1.5
# scale = 2

# screen = pygame.display.set_mode((240, 240))

# rocket = pygame.image.load("images/00.png")
# rocket = pygame.transform.scale(rocket, (rocket.get_width() * scale, rocket.get_height() * scale))
# rocket_rect = rocket.get_rect()
# clock = pygame.time.Clock()

# moving_right_flag = False
# moving_left_flag = False
# moving_up_flag = False
# moving_down_flag = False

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("exiting")
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 moving_left_flag = True
#             elif event.key == pygame.K_RIGHT:
#                 moving_right_flag = True
#             elif event.key == pygame.K_UP:
#                 moving_up_flag = True
#             elif event.key == pygame.K_DOWN:
#                 moving_down_flag = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 moving_left_flag = False
#             elif event.key == pygame.K_RIGHT:
#                 moving_right_flag = False
#             elif event.key == pygame.K_UP:
#                 moving_up_flag = False
#             elif event.key == pygame.K_DOWN:
#                 moving_down_flag = False 

#     if moving_left_flag == True:
#         if rocket_rect.left > 0:
#             rocket_rect.x -= 1 + speed
#     if moving_right_flag == True:
#         if rocket_rect.right < screen.get_width():
#             rocket_rect.x += 1 + speed
#     if moving_up_flag == True:
#         if rocket_rect.top > 0:
#             rocket_rect.y -= 1 + speed
#     if moving_down_flag == True:
#         if rocket_rect.bottom < screen.get_height():
#             rocket_rect.y += 1 + speed
    
#     screen.fill((0, 0, 0))
#     screen.blit(rocket, rocket_rect)
#     pygame.display.flip()
#     clock.tick(60)

import pygame

import sys

pygame.init()

screen = pygame.display.set_mode((200, 200))
screen_rect = screen.get_rect()

clock = pygame.time.Clock()

bg_color = (0, 0, 0)

rocket = pygame.image.load("images/ship.bmp")
rocket_rect = rocket.get_rect()
rocket_rect.centerx = screen_rect.centerx
rocket_rect.centery = screen_rect.centery

moving_up = False
moving_down = False
moving_right = False
moving_left = False

speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False
    
    if moving_up and rocket_rect.top > screen_rect.top:
        rocket_rect.y -= 1 + speed
    elif moving_down and rocket_rect.bottom < screen_rect.bottom:
        rocket_rect.y += 1 + speed 
    if moving_right and rocket_rect.right < screen_rect.right:
        rocket_rect.x += 1 + speed
    elif moving_left and rocket_rect.left > screen_rect.left:
        rocket_rect.x -= 1 + speed

    screen.fill(bg_color)
    screen.blit(rocket, rocket_rect)

    pygame.display.flip()

    clock.tick(30)