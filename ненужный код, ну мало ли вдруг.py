"""
class Dima(Agility):
    def __init__(self, _st, _ag, _int, team):
        super().__init__(_st, _ag, _int, team)
        self.skills = [self.baby_rage, self.lucky_boy]

    def baby_rage(self, enemy_hero):
        cur_damage = self.damage + randint(-self.p_num, self.p_num)
        enemy_hero.health -= cur_damage
        self.health -= cur_damage

    def lucky_boy(self, enemy_hero):
        pass
"""