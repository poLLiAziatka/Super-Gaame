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
            team2_surf.blit(team2_text, (7 * size, 2 * size))"""