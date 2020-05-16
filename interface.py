import pygame
from board import Board
from hero import *

FPS = 60
size = 70

background_color = (231, 240, 237)
main_game_color = (127, 185, 194)
button_color_1 = (149, 172, 178)
team1_color = (98, 140, 166)
team2_color = (22, 79, 85)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
pygame.init()
FONT = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

sc = pygame.display.set_mode((size * 16, size * 9))
sc.fill(background_color)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, sc):
        # Blit the text.
        sc.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(sc, self.color, self.rect, 2)

    def get(self):
        return self.text


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
        pygame.draw.rect(sc, main_game_color, (4 * size, 2 * size, 6 * size, 2 * size))
        pygame.draw.rect(sc, button_color_1, (5 * size, 5 * size, 4 * size, 1 * size))
        pygame.draw.rect(sc, button_color_1, (5 * size, 6 * size, 4 * size, 1 * size))

        pygame.display.update()
        clock.tick(FPS)


def team_name_and_field_size():
    input_box1 = InputBox(size * 7, size, size * 6, size)
    input_box2 = InputBox(size * 7, size * 2, size * 6, size)
    input_box3 = InputBox(size * 7, size * 3, size * 6, size)
    input_box4 = InputBox(size * 7, size * 4, size * 6, size)
    input_boxes = [input_box1, input_box2, input_box3, input_box4]
    while 1:
        pos = pygame.mouse.get_pos()

        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        name_team1 = input_box1.get()
                        name_team2 = input_box2.get()
                        x_size_field = int(input_box3.get())
                        y_size_field = int(input_box4.get())

                        heroes_func(name_team1, name_team2, x_size_field, y_size_field)
            for box in input_boxes:
                box.handle_event(i)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(sc)

        f1 = pygame.font.SysFont('serif', size // 10 * 8)
        f2 = pygame.font.SysFont('serif', size // 10 * 3)
        team1_text = f1.render('Name team 1: ', 1, team1_color)
        team2_text = f1.render('Name team 2: ', 1, team2_color)
        fieldx_text = f1.render('Length field: ', 1, button_color_1)
        fieldy_text = f1.render('Width field: ', 1, button_color_1)

        txt_info = f2.render('Убедительная просьба, в полях Length field и Width field писать целые числа от 6 до 10. '
                             'Иначе горите в аду.', 1, (0, 0, 0))

        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (size, 2 * size))
        sc.blit(fieldx_text, (size, 3 * size))
        sc.blit(fieldy_text, (size, 4 * size))
        sc.blit(txt_info, (size, 7 * size))

        pygame.draw.rect(sc, button_color_1, (13 * size, 8 * size, 3 * size, 1 * size))

        pygame.display.update()
        clock.tick(FPS)


def heroes_func(name_team1, name_team2, x_size_field, y_size_field):
    characters = ['Инженер', "Глава ОПГ Жележные рукова", "Журналист", "Шершняга", "Роза Робот", "Катаморанов"]
    input_boxes = []
    for i in range(len(characters)):
        k = 0.35
        input_box = InputBox(6 * size + 20, (i + 2) * size, size * k, size * k)
        input_box1 = InputBox(7 * size + 20, (i + 2) * size, size * k, size * k)
        input_box2 = InputBox(13 * size + 20, (i + 2) * size, size * k, size * k)
        input_box3 = InputBox(14 * size + 20, (i + 2) * size, size * k, size * k)
        input_boxes.append(input_box)
        input_boxes.append(input_box1)
        input_boxes.append(input_box2)
        input_boxes.append(input_box3)

    while 1:
        sc.fill(background_color)

        pos = pygame.mouse.get_pos()

        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        coordinates = []
                        for input_box in input_boxes:
                            coordinates.append(int(input_box.get()))
                        game(name_team1, name_team2, x_size_field, y_size_field, coordinates)
            for box in input_boxes:
                box.handle_event(i)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(sc)

        f1 = pygame.font.SysFont('serif', size // 10 * 3)
        f2 = pygame.font.SysFont('serif', size // 10 * 3)
        team1_text = f1.render(name_team1, 1, team1_color)
        team2_text = f1.render(name_team2, 1, team2_color)

        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (8 * size, size))
        j = 1
        for character in characters:
            j += 1
            sc.blit(f1.render(character, 1, team1_color), (size, j * size))
            sc.blit(f1.render(character, 1, team2_color), (8 * size, j * size))
            sc.blit(f1.render("x: ", 1, button_color_1), (6 * size, j * size))
            sc.blit(f1.render("y: ", 1, button_color_1), (7 * size, j * size))
            sc.blit(f1.render("x: ", 1, button_color_1), (13 * size, j * size))
            sc.blit(f1.render("y: ", 1, button_color_1), (14 * size, j * size))

        txt_info = f2.render(f' х не должно превышать {x_size_field}; y {y_size_field}', 1, (0, 0, 0))
        sc.blit(txt_info, (size, 8 * size))

        pygame.draw.rect(sc, button_color_1, (13 * size, 8 * size, 3 * size, 1 * size))
        pygame.display.update()
        clock.tick(FPS)


def game(name_team1, name_team2, x_size_field, y_size_field, coordinates):
    if not coordinates:
        coordinates = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 2, 1, 2, 2, 3, 2, 4, 2, 5, 2, 6]
    board = Board(x_size_field, y_size_field)
    heroes_team_0 = []
    heroes_team_1 = []

    engineer_0 = Engineer(12, 30, 8, name_team1)
    engineer_1 = Engineer(12, 30, 8, name_team2)
    heroes_team_0.append(engineer_0)
    heroes_team_1.append(engineer_1)

    lis_0 = Leader_iron_sleeves(15, 25, 10, name_team1)
    lis_1 = Leader_iron_sleeves(15, 25, 10, name_team2)
    heroes_team_0.append(lis_0)
    heroes_team_1.append(lis_1)

    journalist_0 = Journalist()
    journalist_1 = Journalist()
    heroes_team_0.append(journalist_0)
    heroes_team_1.append(journalist_1)

    shershnyga_0 = Shershnyga()
    shershnyga_1 = Shershnyga()
    heroes_team_0.append(shershnyga_0)
    heroes_team_1.append(shershnyga_1)

    katamaronov_0 = Katamaronov(26, 10, 14, name_team1)
    katamaronov_1 = Katamaronov(26, 10, 14, name_team2)
    heroes_team_0.append(katamaronov_0)
    heroes_team_1.append(katamaronov_1)

    rosa_0 = Rosa_robot(29, 11, 10, name_team1)
    rosa_1 = Rosa_robot(29, 11, 10, name_team2)
    heroes_team_0.append(rosa_0)
    heroes_team_1.append(rosa_1)
    heroes = heroes_team_0 + heroes_team_1

    i = 0
    for hero in heroes:
        board.add(hero, coordinates[i], coordinates[i + 1])
        i += 2

    while 1:
        sc.fill(background_color)
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()

        for i in range(x_size_field):
            pygame.draw.line(sc, main_game_color, [(i + 1) * size, (i + 1) * size], [(i + 1) * size, 9 * size], 3)

    pygame.display.update()
    clock.tick(FPS)


main_menu()
