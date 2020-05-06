import pygame
import pygame_textinput

FPS = 60
size = 60

background_color = (231, 240, 237)
name_game_color = (127, 185, 194)
button_color_1 = (149, 172, 178)
team1_color = (98, 140, 166)
team2_color = (22, 79, 85)


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
        pygame.draw.rect(sc, button_color_1, (5 * size, 5 * size, 4 * size, 1 * size))
        pygame.draw.rect(sc, button_color_1, (5 * size, 6 * size, 4 * size, 1 * size))

        pygame.display.update()
        clock.tick(FPS)


def team_name_and_field_size():

    active_team2 = False
    active_team1 = False
    name_team1 = ''
    name_team2 = ''
    team1_input = pygame_textinput.TextInput(initial_string=name_team1, font_family='serif', font_size=size // 10 * 8,
                                             text_color=team1_color, cursor_color=team1_color)
    team2_input = pygame_textinput.TextInput(initial_string='', font_family='serif', font_size=size // 10 * 8,
                                             text_color=team2_color, cursor_color=team2_color)
    while 1:
        pos = pygame.mouse.get_pos()

        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT: exit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        heroes(name_team1, name_team2)
                    elif size * 7 <= pos[0] <= size * 12 and 1 * size <= pos[1] <= 2 * size:
                        active_team1 = True
                        active_team2 = False

                    elif size * 7 <= pos[0] <= size * 12 and 2 * size <= pos[1] <= 3 * size:
                        active_team2 = True
                        active_team1 = False

                    elif team1_input.update(events):
                        name_team1 = team1_input.get_text()
                        print(name_team1)
                    elif team2_input.update(events):
                        name_team2 = team2_input.get_text()



        team1_surf = pygame.Surface((size * 6, size))
        team1_surf.fill((255, 255, 255))

        team2_surf = pygame.Surface((size * 6, size))
        team2_surf.fill((255, 255, 255))

        sc.blit(team1_surf, (7 * size, size - 5))
        sc.blit(team2_surf, (7 * size, 2 * size))

        if active_team1:
            team1_input.update(events)
            sc.blit(team1_input.get_surface(), (size * 7, size))
            team1_text = f1.render(name_team1, 1, team1_color)
            team2_text = f1.render('', 1, team2_color)
            team1_surf.blit(team1_text, (7 * size, size))
            team2_surf.blit(team2_text, (7 * size, 2 * size))

        elif active_team2:
            team2_input.update(events)
            sc.blit(team2_input.get_surface(), (size * 7, 2 * size))
            team1_text = f1.render('', 1, team1_color)
            team2_text = f1.render(name_team2, 1, team2_color)
            team1_surf.blit(team1_text, (7 * size, size))
            team2_surf.blit(team2_text, (7 * size, 2 * size))

        f1 = pygame.font.SysFont('serif', size // 10 * 8)
        team1_text = f1.render('Name team 1: ', 1, team1_color)
        team2_text = f1.render('Name team 2: ', 1, team2_color)
        fieldx_text = f1.render('Length field: ', 1, button_color_1)
        fieldy_text = f1.render('Width field: ', 1, button_color_1)

        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (size, 2 * size))
        sc.blit(fieldx_text, (size, 3 * size))
        sc.blit(fieldy_text, (size, 4 * size))

        pygame.draw.rect(sc, button_color_1, (13 * size, 8 * size, 3 * size, 1 * size))

        pygame.display.update()
        clock.tick(FPS)


def heroes(name_team1, name_team2):
    while 1:

        sc.fill(background_color)

        pos = pygame.mouse.get_pos()

        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        game()

        f1 = pygame.font.SysFont('serif', size // 10 * 3)
        team1_text = f1.render(name_team1, 1, team1_color)
        team2_text = f1.render(name_team2, 1, team2_color)
        characters = ['Инженер', "Глава ОПГ Жележные рукова", "Журналист", "Шершняга", "Роза Робот", "Катаморанов"]
        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (8 * size, size))
        i = 1
        for character in characters:
            i += 1
            sc.blit(f1.render(character, 1, team1_color), (size, i * size))
            sc.blit(f1.render(character, 1, team2_color), (8 * size, i * size))
            sc.blit(f1.render("x: ", 1, button_color_1), (6 * size, i * size))
            sc.blit(f1.render("y: ", 1, button_color_1), (7 * size, i * size))
            sc.blit(f1.render("x: ", 1, button_color_1), (13 * size, i * size))
            sc.blit(f1.render("y: ", 1, button_color_1), (14 * size, i * size))

        pygame.draw.rect(sc, button_color_1, (13 * size, 8 * size, 3 * size, 1 * size))
        pygame.display.update()
        clock.tick(FPS)


def game():
    pass


main_menu()
