import random


class Board:
    def __init__(self, x_size, y_size):
        self.field = [[0] * y_size for _ in range(x_size)]
        self.x_size = x_size
        self.y_size = y_size

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
        return [self.x_size, self.y_size]

    # надо переписать
    def move(self, hero, st, num):
        flag = False
        if 0 < num < 2:
            for i in range(self.x_size):
                for j in range(self.y_size):
                    if self.field[i][j] == hero:
                        if st == 'направо':
                            self.check_move(i + num, j, hero, i, j)  # self.check_move(i + num - 1, j, hero)
                            flag = True
                        elif st == 'налево':
                            self.check_move(i - num, j, hero, i, j)
                            flag = True
                        elif st == 'вверх':
                            self.check_move(i, j - num, hero, i, j)
                            flag = True
                        elif st == 'вниз':
                            self.check_move(i, j + num, hero, i, j)
                            flag = True
                        else:
                            print('Неправильно задана команда')
                if flag:
                    break
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
        if self.field[x][y] != 0:
            self.field[i][j] = hero_1
            self.battle(hero_1, self.field[x][y])  # сначала, кто встал на клетку, потом кто был там
        elif self.field[x][y] == 0:
            self.field[x][y] = hero_1
            self.field[i][j] = 0

    def __str__(self):
        return str(self.field)

    # эта функция нахер не нужна
    def game(self, team):
        while True:
            # check team
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

    def battle(self, attacking, defending):
        print('oooh yeaa')
        attacking.attack = random.randint(1, attacking._st)
        print(attacking.attack)
        defending.bias = defending.health / 5 * 8
        print(defending.bias)

        if random.randint(0, 100) in [x for x in range(int(defending.bias))]:
            print('Уворот')
            i = random.randint(0, 1)
            attacking.skills[i]
            attacking.attack = 0

        attacking.sk_pr = attacking._int / 5 * 7
        print(attacking.sk_pr)

        if random.randint(0, 100) in [x for x in range(int(attacking.sk_pr))]:
            print('Skill')
            i = random.randint(0, 1)
            attacking.skills[i]
        '''
        attacking.sd = attacking._ag / 5 * 6
        print(attacking.sd )
        if random.randint(0, 100) in [x for x in range(int(attacking.sd))]:
            print()
            i = random.randint(0, 1)
            attacking.skills[i]
        '''
        defending.health -= attacking.attack

        defending.attack = random.randint(1, defending._st)
        #  оно как-то работает, но я хз как

#  board должен знать кто ходит
# проверить пустая ли клетка, если на клетке враг - сражение:
#  проверить status_move: Полина
