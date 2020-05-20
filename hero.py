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
        self.health = self._st * 25
        self.p_iv = self._ag / 50 * 80
        self.p_mag = self._int / 50 * 70
        self.freeze = 0

    def ability_to_move(self):
        if self.freeze == 0:
            return True
        else:
            self.freeze -= 1
            return False

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
        return Image.open('1.jpg')

    def __str__(self):
        return 'Инженер'

    def description(self):
        return 'Неуверенный в себе, непутевый, меланхоличный инженер НИИ, который разрабатывает секретные сыворотки и проводит генетические эксперименты. Часто он становится героем неловких, а иногда опасных ситуаций, или просто рассуждает о жизни'


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
        return Image.open('2.jpg')

    def __str__(self):
        return 'Глава ОПГ железные рукава'

    def description(self):
        return 'ОПГ «Железные рукава», которая помимо преступной деятельности занимается и музыкальной. Их дело пытается расследовать ведущий передачи «Загадка дыры», но не добивается успеха'


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
        return Image.open('3.jpg')

    def __str__(self):
        return 'Катамаранов'

    def description(self):
        return 'Водитель асфальтового катка, одноклассник инженера и алкоголик Игорь Катамаранов. Его жену Зинку Кашину, управляющую отделения нейротрансплантологии НИИ, засосало в трубу.'


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
        return Image.open('4.jpg')

    def __str__(self):
        return 'Роза Робот'

    def description(self):
        return 'Рок-группа «Багровый фантомас», состоящая из Розы Робота и Шершняги. Герои, чей образ основан на фанатах российской рок-музыки 90-х, мечтают стать популярными и разговаривают на молодёжном сленге, постоянно употребляя слово «блин»'


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
        return Image.open('5.jpg')

    def __str__(self):
        return 'Шершняга'

    def description(self):
        return 'Рок-группа «Багровый фантомас», состоящая из Розы Робота и Шершняги. Герои, чей образ основан на фанатах российской рок-музыки 90-х, мечтают стать популярными и разговаривают на молодёжном сленге, постоянно употребляя слово «блин»'


class Journalist(Strength):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.degrade, self.run]

    def degrade(self, hero):
        self.damage *= 0.7

    def run(self, hero, _ag):
        if _ag <= 7:
            _ag += 2

    def image(self):
        return Image.open('6.jpg')

    def __str__(self):
        return 'Журналист'

    def description(self):
        return 'Ведущий телепередачи «Сдохни или умри». «Сдохни или умри» — это пародия на шоу о выживании в дикой природе, только здесь герой пытается выжить в метро, канализации или лесу с «заброшенными собаками»'
