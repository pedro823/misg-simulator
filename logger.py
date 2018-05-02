import datetime
import math
import json
import os
import os.path
from util import is_windows, unix_to_nt
class Logger:

    def __init__(self, logfile):
        if is_windows():
            log_file = unix_to_nt(log_file)
        folder = os.path.abspath(os.path.join(logfile, os.pardir))
        if not os.path.exists(folder):
            os.mkdir(folder)
        self.f = open(logfile, 'w+')
        self.date = datetime.datetime.now()

    def log_header(self):
        self.__log_spacer()
        self.f.write(self.__center('RELATÓRIO DA BATALHA') + '\n')
        self.f.write(self.__center(str(self.date.date())) + '\n')
        self.f.write(self.__center(str(self.date.time())) + '\n')
        self.__log_spacer()

    def log_initial_position(self, a_units, b_units, game_scenario):
        unit_total_a = dict()
        unit_total_b = dict()
        for unit in a_units:
            if unit_total_a.get(unit.type) is None:
                unit_total_a[unit.type] = 0
            unit_total_a[unit.type] += unit.multiple
        for unit in b_units:
            if unit_total_b.get(unit.type) is None:
                unit_total_b[unit.type] = 0
            unit_total_b[unit.type] += unit.multiple
        self.f.write(self.__center('POSIÇÃO INICIAL DE TROPAS') + '\n')
        self.__log_spacer()
        self.f.write('Nação A:\n')
        self.f.write(json.dumps(unit_total_a, indent=4) + '\n')
        self.f.write('Nação B:\n')
        self.f.write(json.dumps(unit_total_b, indent=4) + '\n')
        self.f.write('Cenário inicial:\n    Sorte: ' + str(game_scenario.luck) + '\n')
        self.f.write('    Multiplicador previsto para A: ' + str(round(game_scenario.a_multiplier, 3)) + '\n')
        self.f.write('    Multiplicador previsto para B: ' + str(round(game_scenario.b_multiplier, 3)) + '\n')

    def log_final_position(self, a_units, b_units, game_scenario):
        unit_total_a = dict()
        unit_total_b = dict()
        for unit in a_units:
            if unit_total_a.get(unit.type) is None:
                unit_total_a[unit.type] = 0
            unit_total_a[unit.type] += unit.multiple
        for unit in b_units:
            if unit_total_b.get(unit.type) is None:
                unit_total_b[unit.type] = 0
            unit_total_b[unit.type] += unit.multiple
        self.__log_spacer()
        self.f.write(self.__center('ROUNDS TOTAIS: ' + str(game_scenario.rounds_passed)) + '\n')
        self.f.write(self.__center('POSIÇÃO FINAL DE TROPAS') + '\n')
        self.__log_spacer()
        if len(unit_total_a) == 0:
            self.f.write(self.__center('Tropas da nação A foram DIZIMADAS.') + '\n')
        else:
            self.f.write('Nação A:\n')
            self.f.write(json.dumps(unit_total_a, indent=4) + '\n')
        if len(unit_total_b) == 0:
            self.f.write(self.__center('Tropas da nação B foram DIZIMADAS.') + '\n')
        else:
            self.f.write('Nação B:\n')
            self.f.write(json.dumps(unit_total_b, indent=4) + '\n')
        self.f.close()

    def log_retreat(self, team, a_units, b_units, game_scenario, status):
        self.__log_spacer()
        nation = ' A' if team == 1 else ' B'
        status_dict = {
            'success': 'A retirada foi um sucesso.',
            'damaged': 'Conseguiram se retirar, mas sofreram causalidades na hora da retirada.',
            'failure': 'Entretanto, não conseguiu se retirar da batalha.'
        }
        self.f.write(self.__center('Após ' + str(game_scenario.rounds_passed) + ' rounds,'
                                   + ' a nação' + nation + ' decidiu recuar.') + '\n')
        self.f.write(self.__center(status_dict[status]) + '\n')
        self.__log_spacer()

    def log_stalemate(self, game_scenario):
        self.__log_spacer()
        self.f.write(self.__center('Após ' + str(game_scenario.rounds_passed) + ' rounds,'
                     + ' nenhuma unidade conseguia se atacar mais.') + '\n')

    # private

    def __log_spacer(self):
        self.f.write('+' + '-' * 78 + '+\n')

    @staticmethod
    def __center(string):
        half_spacing = (80 - len(string)) / 2
        return ' ' * math.floor(half_spacing) + str(string) + ' ' * math.ceil(half_spacing)

# Unit testing
if __name__ == '__main__':
    from gameloop import *
    a_units, b_units, game_scenario = parse_battle_info()
    log = Logger('logs/unit_test.txt')
    log.log_header()
    log.log_initial_position(a_units, b_units, game_scenario)
