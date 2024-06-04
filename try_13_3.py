import pygame

import sys

from pygame.sprite import Sprite

pygame.init()

screen = pygame.display.set_mode((400, 400))

clock = pygame.time.Clock()

rain_speed = 1

# create rain object
class Rain(Sprite):
    """create rain object"""
    def __init__(self):
        """initialise rains and its starting position"""
        super().__init__()
        self.image = pygame.image.load("images/00.png").convert()
        self.rect = self.image.get_rect()

def _update_position(rains):
    """update rain position"""
    for rain in rains:
        rain.rect.y += rain_speed

def _create_rain():
    rain = Rain()
    rain_width, rain_height = rain.rect.size
    current_x = 0
    current_y = 0
    screen_rect = screen.get_rect()

    while (current_y < 3 * rain_height):
        while (current_x < screen_rect.right):
            rain = Rain()
            rain.rect.x = current_x
            rain.rect.y = current_y
            rains.add(rain)

            current_x += 2 * rain.rect.width
        
        current_x = 0
        current_y += rain_height

def _check_rain_(rains):
    for rain in rains.copy():
        if rain.rect.bottom > screen.get_height():
            rains.remove(rain)


# create grid of rains
rains = pygame.sprite.Group()
_create_rain()


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass



    _update_position(rains)
    _check_rain_(rains)

    if not rains:
        _create_rain()

    screen.fill((0, 0, 0))
    rains.draw(screen)

    pygame.display.flip()

    print(rains)

    clock.tick(60)



