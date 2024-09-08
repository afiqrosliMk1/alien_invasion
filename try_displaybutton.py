# #NOTE: 12/8/2024. After leaving pygame for long time,
# #I just decide to refresh my memory on basics pygame architecture by making this script

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((400, 400))
# pygame.display.set_caption("drawing triangle rect example")

# clock = pygame.time.Clock()

# while True:
#     # process player input
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
        
#     # Do logical updates here
#     # ...
#     button_rect = pygame.Rect(0, 0, 20, 20)
#     button_color = (120, 120, 120)

#     screen.fill("lightblue")

#     # Render the graphics here
#     # ...
#     #pygame.draw.rect(screen, button_color, button_rect)
#     pygame.draw.polygon(screen, button_color, [(0, 0), (0, 200), (200, 100)])

#     pygame.display.flip()
#     clock.tick(60)


import pygame

import sys

pygame.init()

screen = pygame.display.set_mode((200, 200))
screen_rect = screen.get_rect()
screen.fill((25, 50, 100))

square = pygame.Rect(0, 0, 20, 20)
square.centerx = screen_rect.centerx
square.centery = screen_rect.centery

image = pygame.image.load("images/ship.bmp")

clock = pygame.time.Clock()
direction = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((25, 50, 100))
    if direction == 1:
        if square.right < screen_rect.right:
            square.centerx += 1
        else:
            direction = -1
    else:
        if square.left > screen_rect.left:
            square.centerx -= 1
        else:
            direction = 1

    pygame.draw.rect(screen, (255, 0, 0), square)
    screen.blit(image, (0, 0))
    pygame.display.flip()
    clock.tick(60)

 