#delete this later - try 12-2
# import pygame
# import sys

# SCALE = 8

# pygame.init()

# screen = pygame.display.set_mode((240, 240))
# screen.fill((0, 255, 0))
# player = pygame.image.load("images/00.png").convert()
# scaled_player = pygame.transform.scale(player, (player.get_width() * SCALE, player.get_height() * SCALE))

# scaled_player.set_colorkey((0, 0, 0))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.blit(scaled_player, (((screen.get_width() - scaled_player.get_width()) / 2), ((screen.get_height() - scaled_player.get_height()) / 2)))
#     pygame.display.flip()

import pygame

screen = pygame.display.set_mode((200, 200))
screen_rect = screen.get_rect()
screen.fill("lightblue")

image = pygame.image.load("images/00.png")
color_to_match = image.get_at((6, 10)) #get_at() gives you rgb value at certain location
screen.fill(color_to_match)
image_width = image.get_width()
image_height = image.get_height()
scaled_image = pygame.transform.scale(image, (image_width * 4, image_height * 4))
#image.set_colorkey((255, 255, 255))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    print(str(screen_rect.centerx) + ", " + str(screen_rect.centery))
    screen.blit(scaled_image, (screen_rect.centerx, screen_rect.centery))
    pygame.display.flip()
    clock.tick(60)