import pygame

pygame.init()

size = 50

pygame.display.set_mode((size * 16, size * 9))
""", pygame.FULLSCREEN"""

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
