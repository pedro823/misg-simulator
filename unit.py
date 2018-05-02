import random as r
class Unit:
    """ Defines generically an unit that attacks. """

    cant_attack_dict = {
        'all': [

        ]
    }

    def __init__(self, team, type, hp, ATK, DEF, game_scenario,
                 cannot_attack={},
                 advantage_against={},
                 multiple=1,
                 prob_hit=0.2,
                 condition_to_hit=None):
        """ Valid arguments:
            team: 1 or 2. Which team is this unit on.
            hp: The max health of the unit.
            ATK: the attack power of the unit.
            DEF: The defense power of the unit.
            can_attack: Array-like. What the unit can attack.
            game_scenario: Reference to game scenario class.
        """
        self.team = team
        self.type = type
        self.hp = hp * multiple
        self.single_hp = hp
        self.ATK = ATK
        self.DEF = DEF
        self.game_scenario = game_scenario
        self.prob_hit = prob_hit
        self.multiple = multiple
        # self.cannot_attack = self.develop_cannot_attack(cannot_attack)
        self.cannot_attack = cannot_attack
        self.advantage_against = advantage_against
        if condition_to_hit is None:
            self.condition_to_hit = self.__null_condition
        else:
            self.condition_to_hit = condition_to_hit(self.type)

    def __str__(self):
        return ('<#Unit team=' + str(self.team) + ' type=' + self.type + ' hp=' + str(self.hp)
                              + ' multiple=' + str(self.multiple) + ' ATK=' + str(self.ATK)
                              + ' DEF=' + str(self.DEF) + '>')

    def __repr__(self):
        return ('<#Unit team=' + str(self.team) + ' type=' + self.type + ' hp=' + str(self.hp)
                               + ' multiple=' + str(self.multiple) + ' ATK=' + str(self.ATK)
                               + ' DEF=' + str(self.DEF) + '>')

    def attack(self, other):
        """ Tries and attack the other """
        if not self.is_dead() and other.type not in self.cannot_attack:
            if self.condition_to_hit(self):
                mult = self.game_scenario.a_army_size if self.team == 1 else self.game_scenario.b_army_size
                rand_number = r.random() * mult
                if rand_number > other.prob_hit:
                    print('---')
                    # Hurts 50 to 100% its damage, with luck
                    luck = (self.game_scenario.luck if self.team == 1 else -self.game_scenario.luck) / 5
                    if luck < 0: luck = 0
                    hurt_damage = round(self.ATK * self.multiple * (0.5 + luck + (r.random() / 2)), 0)
                    # advantage_against: adds 10% to the damage
                    if other.type in self.advantage_against: hurt_damage *= 1.1
                    print(self.type, '(team', str(self.team) + ') hit', other.type, 'for', hurt_damage, 'damage')
                    other.hurt(hurt_damage)
                    print(other.type, 'new hp', other.hp)
                    print('---')
            else:
                print(self.type, 'could not attack!')

    def can_attack(self, other):
        return not other.type in self.cannot_attack

    def hurt(self, amount):
        """ Gets hurt amount hp. """
        units_hurt = amount // self.single_hp
        self.multiple -= units_hurt
        if self.multiple < 0: self.multiple = 0
        self.hp -= amount
        if self.hp < 0: self.hp = 0

    def is_dead(self):
        return self.hp <= 0

    # private

    def __null_condition(*args):
        return True
