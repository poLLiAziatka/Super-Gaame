from random import randint
from board import Board
from PIL import Image


class Hero:
    def __init__(self, _st, _ag, _int, team):
        if _st + _ag + _int != 50:
            print("error")
        self._st = _st
        self._ag = _ag
        self._int = _int
        self.team = team
        self.health = self._st * 25
        self.start_health = self._st * 25
        self.p_iv = self._ag / 50 * 80
        self.p_mag = self._int / 50 * 70
        self.freeze = 0

    def move_freeze(self):
        if self.freeze != 0:
            self.freeze -= 1

    def heal(self):
        self.health *= 1.15


class Strength(Hero):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.p_num = 3
        self.damage = _st


class Agility(Hero):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.p_num = 2
        self.damage = _st


class Intelligency(Hero):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.p_num = 4
        self.damage = _st


class Engineer(Intelligency):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.enemy_block, self.degrade]

    def enemy_block(self, enemy):
        self.freeze += 1

    def degrade(self, hero):
        self._int -= 2

    def image(self):
        return "1.jpg"

    def __str__(self):
        return 'Инженер'

    def description(self):
        st = 'Меланхоличный, разрабатывает секретные сыворотки'
        return st

    def team(self):
        return self


class Leader_iron_sleeves(Intelligency):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.double_damage, self.freezing]

    def double_damage(self):
        self.damage *= 2

    def freezing(self):
        lst_freeze = []
        x, y = Board.sizes()
        downx = x - 2
        upx = x + 2
        downy = y - 2
        upy = y + 2
        field = Board.field_return()
        for i in range(downx, upx + 1):
            for j in range(downy, upy + 1):
                if field[i][j] != 0:
                    lst_freeze.append(field[i][j])
        for hero in lst_freeze:
            self.freeze += 2

    def image(self):
        return "2.jpg"

    def __str__(self):
        return 'Глава ОПГ железные рукава'

    def description(self):
        st = 'Руководит ОПГ, за которой следит Журналист'
        return st

    def team(self):
        return self


class Katamaronov(Agility):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.skipidar, self.troubles_with_head]

    def skipidar(self):
        self.damage = int(self.damage * 1.15)

    def troubles_with_head(self):
        damage = self.damage + randint(- self.p_num, self.p_num)
        self.health -= damage

    def image(self):
        return "3.jpg"

    def __str__(self):
        return 'Катамаранов'

    def description(self):
        st = 'Алкоголик, одноклассник инженера'
        return st

    def team(self):
        return self


class Rosa_robot(Agility):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.you_dontknow, self.friend_hit]

    def you_dontknow(self, enemy_hero):
        enemy_hero.intel -= 2

    def friend_hit(self, enemy_hero):
        if enemy_hero == Shershnyga:
            enemy_hero.intel = int(enemy_hero.intel * 0.85)

    def image(self):
        return "4.jpg"

    def __str__(self):
        return 'Роза Робот'

    def description(self):
        st = 'Рок-группа "Багровый фантомас, друг Шершняги"'
        return st

    def team(self):
        return self


class Shershnyga(Strength):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.rosa_beats, self.degrade]

    def degrade(self, hero, _st):
        _st *= 1.15

    def rosa_beats(self, enemy_hero):
        if enemy_hero == Rosa_robot:
            self.freeze += 1

    def image(self):
        return "5.jpg"

    def __str__(self):
        return 'Шершняга'

    def description(self):
        st = 'Рок-группа "Багровый фантомас, друг Розы"'
        return st

    def team(self):
        return self


class Journalist(Strength):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.degrade, self.run]

    def degrade(self, hero):
        self.damage *= 0.7

    def run(self, hero, _int):
        if _int <= 7:
            _int += 2

    def image(self):
        return "6.jpg"

    def __str__(self):
        return 'Журналист'

    def description(self):
        st = 'Ведущий телепередачи "Загадка дыры"'
        return st

    def team(self):
        return self