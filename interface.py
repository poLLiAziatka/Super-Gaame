# я не знаю, что тут происходит и как это хреньь вообще может работает

import pygame
from board import Board
from hero import *

FPS = 60
size = 70

# это цвета, моя самая любимая часть кода
background_color = (231, 240, 237)
main_game_color = (127, 185, 194)
additional_game_color = (149, 172, 178)
team1_color = (98, 140, 166)
team2_color = (22, 79, 85)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
pygame.init()
FONT = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()

sc = pygame.display.set_mode((size * 16, size * 9))
sc.fill(background_color)


# это ввод, позаимствовали у какого-то классного человека, работает и хорошо
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(int(x), int(y), int(w), int(h))
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

    # get я написала сама, какая молодец
    def get(self):
        return self.text

    def empty(self):
        if self.text == '':
            return False
        else:
            return True



# Главное меню
# единственное что работает идеально
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
        pygame.draw.rect(sc, additional_game_color, (5 * size, 5 * size, 4 * size, 1 * size))
        pygame.draw.rect(sc, additional_game_color, (5 * size, 6 * size, 4 * size, 1 * size))

        f1 = pygame.font.SysFont('serif', size // 10 * 16)
        f2 = pygame.font.SysFont('serif', size // 10 * 10)
        txt_name = f1.render('Plапенко', 1, background_color)
        txt_button_start = f2.render('Play', 1, background_color)
        txt_button_exit = f2.render('Exit', 1, background_color)
        pygame.draw.rect(sc, background_color, (4 * size, 6 * size, 7 * size, 6 * size), 5)

        sc.blit(txt_button_start, (6 * size + 5, 5 * size - 5))
        sc.blit(txt_button_exit, (6 * size + 5, 6 * size))
        sc.blit(txt_name, (4 * size + 5, 2 * size))

        pygame.display.update()
        clock.tick(FPS)


# ввод названий команд и размеров поля
# не работает удаление текста в вводе
def team_name_and_field_size():
    input_box1 = InputBox(size * 7, size, size * 6, size)
    input_box2 = InputBox(size * 7, size * 2, size * 6, size)
    input_box3 = InputBox(size * 7, size * 3, size * 6, size)
    input_boxes = [input_box1, input_box2, input_box3]
    while 1:
        pos = pygame.mouse.get_pos()

        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size and input_box1.empty() and input_box2.empty() and input_box3.get().isdigit():
                        if 5 < int(input_box3.get()) < 11:
                            # здесь ошибка
                            name_team1 = input_box1.get()
                            name_team2 = input_box2.get()
                            x_size_field = int(input_box3.get())
                            y_size_field = x_size_field

                            heroes_func(name_team1, name_team2, x_size_field, y_size_field)
            for box in input_boxes:
                box.handle_event(i)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(sc)

        f1 = pygame.font.SysFont('serif', size // 10 * 8)
        f2 = pygame.font.SysFont('serif', size // 10 * 3)
        f3 = pygame.font.SysFont('serif', size // 10 * 7)
        team1_text = f1.render('Name team 1: ', 1, team1_color)
        team2_text = f1.render('Name team 2: ', 1, team2_color)
        fieldx_text = f1.render('Size field: ', 1, additional_game_color)
        text_continue = f3.render(' Continue', 1, background_color)

        txt_info = f2.render('Убедительная просьба, в поле Size field писать целые числа от 6 до 10. '
                             'Иначе горите в аду.', 1, (0, 0, 0))

        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (size, 2 * size))
        sc.blit(fieldx_text, (size, 3 * size))
        sc.blit(txt_info, (size, 7 * size))

        pygame.draw.rect(sc, additional_game_color, (13 * size, 8 * size, 3 * size, 1 * size))
        sc.blit(text_continue, (13 * size, 8 * size))
        pygame.display.update()
        clock.tick(FPS)


# ввод координат героев
# здесь все работает и слава богу
def heroes_func(name_team1, name_team2, x_size_field, y_size_field):
    characters = ['Инженер', "Глава ОПГ Железные рукава", "Журналист", "Шершняга", "Роза Робот", "Катамаранов"]
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
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size and input_box.empty() and input_box1.empty() and input_box2.empty() and input_box3.empty() and input_box.get().isdigit() and input_box1.get().isdigit() and input_box2.get().isdigit() and input_box3.get().isdigit():
                        if 5 < int(input_box.get()) and int(input_box1.get()) and int(input_box2.get()) and int(input_box3.get())< 11:
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
        f3 = pygame.font.SysFont('serif', size // 10 * 7)

        team1_text = f1.render(name_team1, 1, team1_color)
        team2_text = f1.render(name_team2, 1, team2_color)
        text_continue = f3.render(' Continue', 1, background_color)

        sc.blit(team1_text, (size, size))
        sc.blit(team2_text, (8 * size, size))

        j = 1
        for character in characters:
            j += 1
            sc.blit(f1.render(character, 1, team1_color), (size, j * size))
            sc.blit(f1.render(character, 1, team2_color), (8 * size, j * size))
            sc.blit(f1.render("x: ", 1, additional_game_color), (6 * size, j * size))
            sc.blit(f1.render("y: ", 1, additional_game_color), (7 * size, j * size))
            sc.blit(f1.render("x: ", 1, additional_game_color), (13 * size, j * size))
            sc.blit(f1.render("y: ", 1, additional_game_color), (14 * size, j * size))

        txt_info = f2.render(f' х и у не должны превышать {x_size_field}', 1, (0, 0, 0))
        sc.blit(txt_info, (size, 8 * size))

        pygame.draw.rect(sc, additional_game_color, (13 * size, 8 * size, 3 * size, 1 * size))
        sc.blit(text_continue, (13 * size, 8 * size))
        pygame.display.update()
        clock.tick(FPS)


# не хочет работать
# у меня не работает голова, чтобы написать формулы для поля
# я тупой пенечек, что вы от меня хотите
def game(name_team1, name_team2, x_size_field, y_size_field, coordinates):
    possible_move = []
    heroes_rect = []
    rects = []
    active_team = name_team1
    for i in range(len(coordinates)):
        coordinates[i] -= 1

    def step():
        nonlocal active_team
        if active_team == name_team1:
            active_team = name_team2
        else:
            active_team = name_team1

        print(active_team)

        for hero in heroes:
            if hero.health != hero.start_health:
                hero.heal()
            hero.move_freeze()

    def info_hero(hero):
        f1 = pygame.font.SysFont('serif', size // 2)
        f2 = pygame.font.SysFont('serif', size // 4)

        txt_hero = f1.render(str(hero), 1, main_game_color)
        twt_team = f2.render(f'команда: {hero.team}', 1, main_game_color)
        txt_health = f2.render('Здоровье:  ', 1, additional_game_color)
        pygame.draw.rect(sc, (255, 0, 0), (int(size * 12.5), size * 4, hero.health, size // 4), 1)
        txt_st = f2.render(f'Сила: {hero._st} ', 1, additional_game_color)
        txt_ag = f2.render(f'Ловкость: {hero._ag} ', 1, additional_game_color)
        txt_int = f2.render(f'Интеллект: {hero._int} ', 1, additional_game_color)
        txt_info = f2.render(hero.description(), 1, (10, 40, 140))

        # тут должна быть картинка
        image = pygame.image.load(hero.image()).convert_alpha()
        new_image = pygame.transform.scale(image, (size * 2, size * 2))

        pygame.draw.rect(sc, (0, 0, 0), (int(size * 11.5), int(size * 1.5), size * 2, size * 2), 1)
        sc.blit(twt_team, (size * 12, size))
        sc.blit(new_image, (int(size * 11.5), int(size * 1.5)))
        sc.blit(txt_info, (size * 10, size * 6))
        sc.blit(txt_hero, (size * 10, size // 2))
        sc.blit(txt_health, (size * 11, size * 4))
        sc.blit(txt_st, (size * 11, int(size * 4.5)))
        sc.blit(txt_ag, (size * 11, size * 5))
        sc.blit(txt_int, (size * 11, int(size * 5.5)))

    if not coordinates:
        coordinates = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
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

    journalist_0 = Journalist(11, 16, 23, name_team1)
    journalist_1 = Journalist(11, 16, 23, name_team2)
    heroes_team_0.append(journalist_0)
    heroes_team_1.append(journalist_1)

    shershnyga_0 = Shershnyga(17, 6, 27, name_team1)
    shershnyga_1 = Shershnyga(17, 6, 27, name_team2)
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

    # ааааа, я заколебалась писать это все

    i = 0
    #  вот здесь фигня какая-то
    s_x = min(size // x_size_field * 6, size // y_size_field * 10)
    # s_y = size // y_size_field * 10
    for hero in heroes:
        board.add(hero, coordinates[i], coordinates[i + 1])
        i += 2

    active_rect = None

    while 1:

        sc.fill(background_color)
        pos = pygame.mouse.get_pos()

        # из-за фигни выше не правильно отрисовывается
        for i in range(x_size_field + 1):
            pygame.draw.line(sc, main_game_color, [i * s_x + size, size], [i * s_x + size, (y_size_field + 1) * s_x], 3)

        for i in range(y_size_field + 1):
            pygame.draw.line(sc, main_game_color, [size, i * s_x + size], [(x_size_field + 1) * s_x, size + i * s_x], 3)

        for i in range(len(board.field)):
            for j in range(len(board.field[i])):
                if board.field[i][j] in heroes:
                    image = pygame.image.load(board.field[i][j].image()).convert_alpha()
                    new_image = pygame.transform.scale(image, (s_x, s_x))

                    rect = pygame.Rect((size + i * s_x, size + j * s_x), (s_x, s_x))
                    if board.field[i][j].health > 0:
                        surf = pygame.Surface((s_x, s_x))

                        surf.blit(new_image, (0, 0))
                        sc.blit(surf, rect)

                        heroes_rect.append([board.field[i][j], rect])
                        rects.append(rect)

        if active_rect is not None:
            possible_move = []
            for i in range(len(board.field)):
                for j in range(len(board.field[i])):
                    if active_rect is not None:
                        # поправить правую стенку
                        if board.field[i][j] == active_rect[0]:
                            # право
                            if i != x_size_field - 1:
                                #print(i)
                                #print(x_size_field)
                                rect = pygame.Rect((size + (i + 1) * s_x, size + j * s_x), (s_x, s_x))
                                surf = pygame.Surface((s_x, s_x))
                                surf.fill((255, 130, 110))
                                surf.set_alpha(150)
                                sc.blit(surf, rect)
                                possible_move.append([rect, 'направо'])
                            # низ
                            if j != y_size_field - 1:
                                rect = pygame.Rect((size + (i) * s_x, size + (j + 1) * s_x), (s_x, s_x))
                                surf = pygame.Surface((s_x, s_x))
                                surf.fill((255, 130, 110))
                                surf.set_alpha(150)
                                sc.blit(surf, rect)
                                possible_move.append([rect, 'вниз'])
                            # верх
                            if j != 0:
                                rect = pygame.Rect((size + (i) * s_x, size + (j - 1) * s_x), (s_x, s_x))
                                surf = pygame.Surface((s_x, s_x))
                                surf.fill((255, 130, 110))
                                surf.set_alpha(150)
                                sc.blit(surf, rect)
                                possible_move.append([rect, 'вверх'])
                            if i != 0:
                                rect = pygame.Rect((size + (i - 1) * s_x, size + (j) * s_x), (s_x, s_x))
                                surf = pygame.Surface((s_x, s_x))
                                surf.fill((255, 130, 110))
                                surf.set_alpha(150)
                                sc.blit(surf, rect)
                                possible_move.append([rect, 'налево'])

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    for move in possible_move:
                        if move[0].collidepoint(pos):
                            for rect in heroes_rect:
                                if rect == active_rect:
                                    print(rect[0])
                                    if rect[0].team == active_team and rect[0].freeze == 0:
                                        board.move(rect[0], move[1], 1)
                                        step()
                                        active_rect = None
                                        heroes_rect = []

                    for rect in heroes_rect:
                        if rect[1].collidepoint(pos):
                            active_rect = rect
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        main_menu()

        f3 = pygame.font.SysFont('serif', size // 10 * 8)
        f4 = pygame.font.SysFont('serif', size // 10 * 6)
        text_continue = f3.render('  Finish', 1, background_color)
        text_team = f4.render(f'Ход команды: {active_team}', 1, team1_color)
        sc.blit(text_team, (size, size // 6))
        pygame.draw.rect(sc, additional_game_color, (13 * size, 8 * size, 3 * size, 1 * size))
        sc.blit(text_continue, (13 * size, 8 * size))

        if not heroes_team_1:
            final(heroes_team_0)
        elif not heroes_team_0:
            final(heroes_team_1)

        if active_rect is not None:
            info_hero(active_rect[0])

        pygame.display.update()
        clock.tick(FPS)


def final(win_team):
    while 1:
        sc.fill(background_color)
        pos = pygame.mouse.get_pos()
        for i in pygame.event.get():
            if i.type == pygame.QUIT: exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 13 * size <= pos[0] <= 16 * size and 8 * size <= pos[1] <= 9 * size:
                        main_menu()

        f1 = pygame.font.SysFont('serif', size)
        f2 = pygame.font.SysFont('serif', size + 30)
        f3 = pygame.font.SysFont('serif', size // 10 * 9)

        txt_win = f1.render('Победила команда', 1, main_game_color)
        txt_win_team = f2.render(win_team, 1, main_game_color)
        text_continue = f3.render('  Done', 1, background_color)

        sc.blit(txt_win, (size * 4, size * 2))
        sc.blit(txt_win_team, (size, size * 3))
        pygame.draw.rect(sc, additional_game_color, (13 * size, 8 * size, 3 * size, 1 * size))
        sc.blit(text_continue, (13 * size, 8 * size))
        pygame.display.update()
        clock.tick(FPS)


game('1111', '22222', 5, 5, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2, 1, 3, 1, 4, 1, 5, 5, 1, 5, 2, 5, 3, 5, 4, 5, 5])
# final('Дрима тима')
# main_menu()
