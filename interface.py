import pygame
import sys

size = 50
FPS = 30

pygame.init()
pygame.display.set_mode((size * 16, size * 9))
""", pygame.FULLSCREEN"""
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
