from random import randint
from board import Board


class Hero:
    def __init__(self, _st, _ag, _int, team):
        if _st + _ag + _int != 50:
            print("error")
        self._st = _st
        self._ag = _ag
        self._int = _int
        self.team = team
        self.health = self._st * 5
        self.start_health = self._st * 25
        self.p_iv = self._ag // 50 * 80
        self.p_mag = self._int // 50 * 70
        self.freeze = 0

    def move_freeze(self):
        if self.freeze != 0:
            self.freeze -= 1

    def heal(self):
        self.health += 1


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
        enemy.freeze += 1

    def degrade(self, enemy):
        self._int -= 2

    def image(self):
        return "1.jpg"

    def __str__(self):
        return 'Инженер'

    def description(self):
        st = 'Меланхоличный, разрабатывает секретные сыворотки'
        return st


class Leader_iron_sleeves(Intelligency):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.double_damage, self.no_double_damage]

    def double_damage(self, enemy):
        self.damage *= 2

    def no_double_damage(self, enemy):
        self.damage = self.damage // 2

    def image(self):
        return "2.jpg"

    def __str__(self):
        return 'Глава ОПГ железные рукава'

    def description(self):
        st = 'Руководит ОПГ, за которой следит Журналист'
        return st


class Katamaronov(Agility):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.skipidar, self.troubles_with_head]

    def skipidar(self, enemy):
        self.damage = int(self.damage * 1.15)

    def troubles_with_head(self, enemy):
        damage = self.damage + randint(- self.p_num, self.p_num)
        self.health -= damage

    def image(self):
        return "3.jpg"

    def __str__(self):
        return 'Катамаранов'

    def description(self):
        st = 'Алкоголик, одноклассник инженера'
        return st


class Rosa_robot(Agility):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.you_dontknow, self.friend_hit]

    def you_dontknow(self, enemy_hero):
        enemy_hero._int -= 2

    def friend_hit(self, enemy_hero):
        if enemy_hero == Shershnyga:
            enemy_hero._int = int(enemy_hero._int * 0.85)
            print(enemy_hero._int)
            print(Shershnyga._int)

    def image(self):
        return "4.jpg"

    def __str__(self):
        return 'Роза Робот'

    def description(self):
        st = 'Рок-группа "Багровый фантомас, друг Шершняги"'
        return st


class Shershnyga(Strength):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.rosa_beats, self.degrade]

    def degrade(self, hero):
        print(self._st)
        self._st = int(self._st * 1.15)
        print(self._st)

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


class Journalist(Strength):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.degrade, self.run]

    def degrade(self, hero):
        self.damage = self.damage // 10 * 7

    def run(self, hero):
        if self._ag <= 7:
            self._ag += 2

    def image(self):
        return "6.jpg"

    def __str__(self):
        return 'Журналист'

    def description(self):
        st = 'Ведущий телепередачи "Загадка дыры"'
        return st
