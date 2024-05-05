#delete this later - try 12-2
import pygame
import sys

SCALE = 8

pygame.init()

screen = pygame.display.set_mode((240, 240))
screen.fill((0, 255, 0))
player = pygame.image.load("images/00.png").convert()
scaled_player = pygame.transform.scale(player, (player.get_width() * SCALE, player.get_height() * SCALE))

scaled_player.set_colorkey((0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(scaled_player, (((screen.get_width() - scaled_player.get_width()) / 2), ((screen.get_height() - scaled_player.get_height()) / 2)))
    pygame.display.flip()

