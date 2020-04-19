import pygame

FPS = 60
size = 70

background_color = (255, 255, 255)
name_game_color = (255, 150, 100)
start_button_color = (58, 202, 19)
exit_button_color = (214, 44, 17)

pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((size * 16, size * 9))

while 1:
    sc.fill(background_color)

    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()

    pygame.draw.rect(sc, name_game_color, (4 * size, 2 * size, 6 * size, 2 * size))
    pygame.draw.rect(sc, start_button_color , (5 * size, 5 * size, 4 * size, 1 * size))
    pygame.draw.rect(sc, exit_button_color, (5 * size, 6 * size, 4 * size, 1 * size))

    pygame.display.update()

    clock.tick(FPS)