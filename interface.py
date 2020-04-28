import pygame

FPS = 60
size = 60

background_color = (255, 255, 255)
name_game_color = (255, 150, 100)
start_button_color = (58, 202, 19)
exit_button_color = (214, 44, 17)
team1_color = (233, 0, 58)
team2_color = (162, 239, 0)

pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((size * 16, size * 9))


# Главное меню
def main_menu():
    while 1:
        sc.fill(background_color)
        pos = pygame.mouse.get_pos()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 5 * size <= pos[0] <= 9 * size and 5 * size <= pos[1] <= 6 * size:
                        team_name_and_field_size()
                    elif 5 * size <= pos[0] <= 9 * size and 6 * size <= pos[1] <= 7 * size:
                        exit()
        pygame.draw.rect(sc, name_game_color, (4 * size, 2 * size, 6 * size, 2 * size))
        pygame.draw.rect(sc, start_button_color, (5 * size, 5 * size, 4 * size, 1 * size))
        pygame.draw.rect(sc, exit_button_color, (5 * size, 6 * size, 4 * size, 1 * size))

        pygame.display.update()
        clock.tick(FPS)


def team_name_and_field_size():
    while 1:

        pos = pygame.mouse.get_pos()

        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        heroes()

        f1 = pygame.font.SysFont('serif', 48)
        team1_text = f1.render('Name team 1: ', 1, team1_color)
        team2_text = f1.render('Name team 2: ', 1, team2_color)
        fieldx_text = f1.render('Length field: ', 1, (180, 0, 0))
        fieldy_text = f1.render('Width field: ', 1, (180, 0, 0))
        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (size, 2 * size))
        sc.blit(fieldx_text, (size, 3 * size))
        sc.blit(fieldy_text, (size, 4 * size))

        pygame.draw.rect(sc, start_button_color, (13 * size, 8 * size, 3 * size, 1 * size))

        pygame.display.update()
        clock.tick(FPS)


def heroes():
    while 1:

        sc.fill(background_color)

        pos = pygame.mouse.get_pos()

        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        game()

        f1 = pygame.font.SysFont('serif', 20)
        team1_text = f1.render('Name team 1', 1, team1_color)
        team2_text = f1.render('Name team 2', 1, team2_color)
        characters = ['Инжинер', "Глава ОПГ Жележные рукова", "Журналист", "Шершняга", "Роза Робот", "Катаморанов"]
        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (8 * size, size))
        i = 1
        for character in characters:
            i += 1
            sc.blit(f1.render(character, 1, (123, 32, 21)), (size, i * size))
            sc.blit(f1.render(character, 1, (123, 32, 21)), (8 * size, i * size))
            sc.blit(f1.render("x: ", 1, (0, 0, 0)), (6 * size, i * size))
            sc.blit(f1.render("y: ", 1, (0, 0, 0)), (7 * size, i * size))
            sc.blit(f1.render("x: ", 1, (0, 0, 0)), (13 * size, i * size))
            sc.blit(f1.render("y: ", 1, (0, 0, 0)), (14 * size, i * size))
        i = 1

        pygame.draw.rect(sc, start_button_color, (13 * size, 8 * size, 3 * size, 1 * size))
        pygame.display.update()
        clock.tick(FPS)


def game():
    pass


main_menu()
