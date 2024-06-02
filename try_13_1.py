import pygame

import sys

from pygame.sprite import Sprite

from random import randint

pygame.init()

class Star(Sprite):
    """a star"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/00.png")
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

screen = pygame.display.set_mode((400, 400))

star = Star()
stars = pygame.sprite.Group()

#make a grid of stars - first approach
# for j in range(screen.get_height() // ( 2 * star.height)):
#     for i in range(screen.get_width() // (2 * star.width)):
#         star = Star()
#         random_number = randint(-2, 2)
#         star.rect.x += i * star.width * random_number
#         star.rect.y += j * 2 * star.height
#         stars.add(star)
    
#make grid of stars - second approach
y_position = 0
while y_position < screen.get_height():
    x_position = 0
    while x_position < screen.get_width():
        print(y_position)
        star = Star()
        
        random_number = randint(0, 20)
        x_position += random_number * star.width
        star.rect.x = x_position
        star.rect.y = y_position

        stars.add(star)

    y_position += star.height
    print(f"y: {screen.get_height()}")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_LEFT:
                pass
        
    # for star in stars:
    #     print(star)
    #     screen.blit(star.image, star.rect)
    stars.draw(screen)

    pygame.display.flip()
    
    clock.tick(30)

