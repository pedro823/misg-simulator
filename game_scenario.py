class GameScenario:

    def __init__(self, a_army_size=1, b_army_size=1, luck=0):
        """ Sets default game scenario """
        self.luck = luck
        self.rounds_passed = 0
        self.a_army_size = a_army_size
        self.b_army_size = b_army_size
        self.a_multiplier = self.calculate_mult(self.a_army_size, self.b_army_size) + luck
        self.b_multiplier = self.calculate_mult(self.b_army_size, self.a_army_size) - luck

    def incr_round(self):
        self.rounds_passed += 1

    def calculate_mult(self, my_size, other_size):
        return 1.9 ** ((my_size - other_size) / (my_size + other_size))

    def set_luck(self, new_luck):
        self.luck = new_luck
        self.a_multiplier = self.calculate_mult(self.a_army_size, self.b_army_size) + new_luck
        self.b_multiplier = self.calculate_mult(self.b_army_size, self.a_army_size) - new_luck

    def set_new_army_size(self, new_a_army_size, new_b_army_size):
        self.a_army_size = new_a_army_size
        self.b_army_size = new_b_army_size
        self.a_multiplier = self.calculate_mult(self.a_army_size, self.b_army_size) + self.luck
        self.b_multiplier = self.calculate_mult(self.b_army_size, self.a_army_size) - self.luck

    def __repr__(self):
        return ('<#GameScenario luck=' + str(self.luck) + ' rounds_passed='
                + str(self.rounds_passed) + ' a_army_size=' + str(self.a_army_size)
                + ' b_army_size=' + str(self.b_army_size) + ' a_multiplier=' + str(self.a_multiplier)
                + ' b_multiplier=' + str(self.b_multiplier) + '>')

    def check(self):
        return True
