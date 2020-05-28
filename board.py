import random


def battle(attacking, defending):
    global Hero
    if attacking.team == defending.team:
        return
    lst = []
    hero_1 = defending
    hero_2 = attacking
    for i in range(2):
        flag = False
        attacking = hero_2
        defending = hero_1
        attacking.attack = random.randint(attacking.damage // 2, attacking.damage)
        defending.bias = defending.health // 100

        if random.randint(0, 100) in [x for x in range(int(defending.bias))]:
            attacking.attack = 0

        attacking.sk_pr = attacking._int // 5 * 7

        if random.randint(0, 100) in [x for x in range(int(attacking.sk_pr))]:
            i = random.randint(0, 1)
            attacking.skills[i](defending)
            flag = True
        defending.health -= attacking.attack

        defending.attack = random.randint(1, defending._st)
        if attacking.attack == 0:
            lst.append(f'Персонаж {defending} отклонился от удара персонажа {attacking}')
        elif flag:
            lst.append(f'Cработал скилл персонажа {attacking}, здоровье {defending} именилось на {attacking.attack}')
        else:
            lst.append(f'Персонаж {attacking} ударил персонажа {defending}: - {attacking.attack} здоровья')
        if attacking.health <= 0 or defending.health <= 0:
            lst.append('')
            break
        hero_1 = attacking
        hero_2 = defending
    print(lst)
    return lst


class Board:
    def __init__(self, x_size, y_size):
        self.field = [[0] * y_size for _ in range(x_size)]
        self.x_size = x_size
        self.y_size = y_size
        self.lst = ['', '']

    def add(self, hero, x, y):
        if x >= self.x_size or x < 0 or y > self.y_size < 0:
            print('Bad indexes!')
            return False
        elif self.field[x][y] != 0:
            print('Cell not is empty')
        self.field[x][y] = hero

    def field_return(self):
        return self.field

    def sizes(self):
        return self.x_size, self.y_size

    def move(self, hero, st, num):
        flag = False
        if 0 < num < 2:
            for i in range(self.x_size):
                if flag:
                    break
                for j in range(self.y_size):
                    if self.field[i][j] == hero:
                        if st == 'направо':
                            self.check_move(i + num, j, hero, i, j)
                            flag = True
                            break
                        elif st == 'налево':
                            self.check_move(i - num, j, hero, i, j)
                            flag = True
                            break
                        elif st == 'вверх':
                            self.check_move(i, j - num, hero, i, j)
                            flag = True
                            break
                        elif st == 'вниз':
                            self.check_move(i, j + num, hero, i, j)
                            flag = True
                            break
                        else:
                            print('Неправильно задана команда')
        else:
            print('Неправильное число')

    def check_board(self, x, y):
        if x <= self.x_size and y <= self.y_size:
            return True
        else:
            return False

    def check_move(self, x, y, hero_1, i, j):
        print(x, y)
        print(self.field[x][y])
        if self.field[x][y] != 0 and self.field[x][y].team != self.field[i][j].team:
            self.field[i][j] = hero_1
            self.lst = battle(hero_1, self.field[x][y])
        elif self.field[x][y] == 0:
            self.field[x][y] = hero_1
            self.field[i][j] = 0

    def __str__(self):
        return str(self.field)

    def game(self, team):
        while True:
            count_0 = 0
            count_1 = 0
            for i in range(self.x_size):
                for j in range(self.y_size):
                    if self.field[i][j] != 0:
                        if self.field[i][j].team == 0:
                            count_0 += 1
                        else:
                            count_1 += 1
            if count_0 == 0:
                print('Team 1 win')
                break
            elif count_1 == 0:
                print('Team 2 win')
