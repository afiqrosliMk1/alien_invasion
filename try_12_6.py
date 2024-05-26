import pygame

import sys

import pygame.image

pygame.init()

#create screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("sideway shooter")

#create ship
ship = pygame.image.load("images/ship.bmp").convert()

#rotate image
ship = pygame.transform.rotate(ship, -90)

print(ship.get_at((2, 2)))

#set colorkey
pygame.Surface.set_colorkey(ship, (230, 230, 230))

#get rect
screen_rect = screen.get_rect()
ship_rect = ship.get_rect()

#start the ship at mid left
ship_rect.y = screen_rect.midleft[1] - ship_rect.height / 2

#movement flag
move_up_flag = False
move_down_flag = False

#bullet
bullet_list = []

#speed
speed = 2



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up_flag = True
            elif event.key == pygame.K_DOWN:
                move_down_flag = True
            elif event.key == pygame.K_SPACE:
                if len(bullet_list) < 5:
                    bullet = pygame.Rect(ship_rect.midright[0], ship_rect.midright[1], 8, 3)
                    bullet_list.append(bullet)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up_flag = False
            elif event.key == pygame.K_DOWN:
                move_down_flag = False

    if move_up_flag:
        if ship_rect.y > 0:
            ship_rect.y -= 1 + speed
    if move_down_flag:
        if ship_rect.bottom < screen_rect.height:
            ship_rect.y += 1 + speed

    screen.fill((0, 0, 0))

    if bullet_list:
        for bullet in bullet_list:
            if bullet.x < screen.get_width():
                bullet.x += 1 + speed
                pygame.draw.rect(screen, (251, 25, 25), bullet)
            else:
                bullet_list.remove(bullet)
       # print(len(bullet_list))

    

    screen.blit(ship, ship_rect)

    pygame.display.flip()

    clock.tick(60)



