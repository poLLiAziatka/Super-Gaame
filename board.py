import random


class Board:
    def __init__(self, x_size, y_size):
        self.field = [[0] * int(y_size) for _ in range(int(x_size))]
        self.x_size = x_size
        self.y_size = y_size
        self.status_move = 0

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

    def move(self, hero, st, num):
        if 0 < num < 3:
            for i in range(self.x_size):
                for j in range(self.y_size):
                    if self.field[i][j] == hero:
                        if st == 'направо':
                            self.field[i][j] = 0
                            self.check_move(i + num, j, hero)
                        elif st == 'налево':
                            self.field[i][j] = 0
                            self.check_move(i - num, j, hero)
                        elif st == 'вверх':
                            self.field[i][j] = 0
                            self.check_move(i, j + num, hero)
                        elif st == 'вниз':
                            self.field[i][j] = 0
                            self.check_move(i, j - num, hero)
                        else:
                            print('Неправильно задана команда')
        else:
            print('Неправильное число')

    def check_board(self, x, y):
        if x <= self.x_size and y <= self.y_size:
            return True
        else:
            return False

    def check_move(self, x, y, hero_1):
        if self.field[x][y] != 0:
            self.battle(hero_1, self.field[x][y])  # сначала, кто встал на клетку, потом кто был там
        else:
            self.field[x][y] = hero_1

    # вот это нам наверное не нужно
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
        attacking.attack = random.randint(1, attacking._st)
        defending.bias = defending.healf / 5 * 8

        if random.randint(0, 100) in [x for x in range(defending.bias)]:
            attacking.attack = 0

        attacking.sk_pr = attacking._int / 5 * 7

        if random.randint(0, 100) in [x for x in range(attacking.sk_pr)]:
            pass

        defending.healf -= attacking.attack

        defending.attack = random.randint(1, defending._st)

#  board должен знать кто ходит
# проверить пустая ли клетка, если на клетке враг - сражение:
#  проверить status_move: Полина
