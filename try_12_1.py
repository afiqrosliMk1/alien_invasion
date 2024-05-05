#delete this later - try 12-1
import pygame

pygame.init()

screen = pygame.display.set_mode((240, 240))
pygame.display.set_caption("blue window")

display = pygame.Surface((150, 100))
display.fill((0, 0, 255))

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
    screen.blit(display, (((screen.get_width() / 2) - (display.get_width() / 2)), ((screen.get_height() / 2) - (display.get_height() / 2))))
    pygame.display.flip()