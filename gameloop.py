from game_scenario import GameScenario
from util import is_windows, unix_to_nt
from unit import Unit
import random

def air_force_condition(type):
    def cond(obj):
        try:
            obj.bombs
        except:
            obj.bombs = 12 if type == 'plane' else 4
        if obj.bombs > 0:
            obj.bombs -= 1
            return True
        return False

    return cond

def parse_battle_info(file_name='battle_info/battle_info.json', luck_factor=0):
    import json
    if is_windows():
        file_name = unix_to_nt(file_name)
    a_units = []
    b_units = []
    team_quantities = [0, 0]
    game_scenario = GameScenario(luck=luck_factor)
    army_file = 'troop_info/army.json'
    navy_file = 'troop_info/navy.json'
    af_file = 'troop_info/air_force.json'
    if is_windows():
        army_file = unix_to_nt(army_file)
        navy_file = unix_to_nt(navy_file)
        af_file = unix_to_nt(af_file)

    with open(file_name, 'r') as f:
        data = json.load(f)
    with open(army_file) as f:
        army_data = json.load(f)
    with open(navy_file) as f:
        navy_data = json.load(f)
    with open(af_file) as f:
        air_force_data = json.load(f)

    if len(data) > 2:
        raise Exception('Esse programa foi feito para rodar em apenas dois times.')
    for team_number, item in enumerate(data):
        team = item['team']
        if team == 1:
            v = a_units
        else:
            v = b_units
        # PARSE ARMY
        for idx, army_item in enumerate(item['army']):
            if army_item.get('unit_type') is None:
                raise Exception('army - classe número ' + str(idx+1) + ' não tem unit_type!')
            if army_item.get('quantity') is None:
                raise Exception('army - classe número ' + str(idx+1) + ' não tem quantity!')
            team_quantities[team_number] += army_item['quantity']

            army_type = army_item['unit_type']
            if army_data['classes'].get(army_type) is None:
                raise Exception('Não existe uma classe de exército chamada ' + str(army_type) + '!')

            batch_size = army_data['classes'][army_type]['batch_size']
            batches = army_item['quantity'] // batch_size
            remaining_batch = army_item['quantity'] % batch_size

            for i in range(batches):
                v.append(Unit(
                    team=team,
                    type=army_type,
                    hp=army_data['classes'][army_type]['hp'],
                    ATK=army_data['classes'][army_type]['ATK'],
                    DEF=army_data['classes'][army_type]['DEF'],
                    cannot_attack=set(army_data['classes'][army_type]['cannot_attack']),
                    advantage_against=set(army_data['classes'][army_type]['advantage_against']),
                    game_scenario=game_scenario,
                    prob_hit=army_data['classes'][army_type]['prob_hit'],
                    multiple=batch_size
                ))
            if remaining_batch > 0:
                v.append(Unit(
                    team=team,
                    type=army_type,
                    hp=army_data['classes'][army_type]['hp'],
                    ATK=army_data['classes'][army_type]['ATK'],
                    DEF=army_data['classes'][army_type]['DEF'],
                    cannot_attack=set(army_data['classes'][army_type]['cannot_attack']),
                    advantage_against=set(army_data['classes'][army_type]['advantage_against']),
                    game_scenario=game_scenario,
                    prob_hit=army_data['classes'][army_type]['prob_hit'],
                    multiple=remaining_batch
                ))
        # PARSE NAVY
        for idx, navy_item in enumerate(item['navy']):
            if navy_item.get('unit_type') is None:
                raise Exception('navy - classe número ' + str(idx+1) + ' não tem unit_type!')
            if navy_item.get('quantity') is None:
                raise Exception('navy - classe número ' + str(idx+1) + ' não tem quantity!')
            team_quantities[team_number] += navy_item['quantity']

            navy_type = navy_item['unit_type']
            if navy_data['classes'].get(navy_type) is None:
                raise Exception('Não existe uma classe de exército chamada ' + str(navy_type) + '!')

            batch_size = navy_data['classes'][navy_type]['batch_size']
            batches = navy_item['quantity'] // batch_size
            remaining_batch = navy_item['quantity'] % batch_size
            for i in range(batches):
                v.append(Unit(
                    team=team,
                    type=navy_type,
                    hp=navy_data['classes'][navy_type]['hp'],
                    ATK=navy_data['classes'][navy_type]['ATK'],
                    DEF=navy_data['classes'][navy_type]['DEF'],
                    cannot_attack=set(navy_data['classes'][navy_type]['cannot_attack']),
                    advantage_against=set(navy_data['classes'][navy_type]['advantage_against']),
                    game_scenario=game_scenario,
                    spot=navy_data['classes'][navy_type]['stealth'],
                    prob_hit=navy_data['classes'][navy_type]['prob_hit'],
                    multiple=batch_size
                ))
            if remaining_batch > 0:
                v.append(Unit(
                    team=team,
                    type=navy_type,
                    hp=navy_data['classes'][navy_type]['hp'],
                    ATK=navy_data['classes'][navy_type]['ATK'],
                    DEF=navy_data['classes'][navy_type]['DEF'],
                    cannot_attack=set(navy_data['classes'][navy_type]['cannot_attack']),
                    advantage_against=set(navy_data['classes'][navy_type]['advantage_against']),
                    game_scenario=game_scenario,
                    spot=navy_data['classes'][navy_type]['stealth'],
                    prob_hit=navy_data['classes'][navy_type]['prob_hit'],
                    multiple=remaining_batch
                ))
        # PARSE AIR FORCE
        for idx, af_item in enumerate(item['air_force']):
            if af_item.get('unit_type') is None:
                raise Exception('air_force - classe número ' + str(idx+1) + ' não tem unit_type!')
            if af_item.get('quantity') is None:
                raise Exception('air_force - classe número ' + str(idx+1) + ' não tem quantity!')
            team_quantities[team_number] += af_item['quantity']

            af_type = af_item['unit_type']
            if air_force_data['classes'].get(af_type) is None:
                raise Exception('Não existe uma classe de exército chamada ' + str(af_type) + '!')

            batch_size = air_force_data['classes'][af_type]['batch_size']
            batches = af_item['quantity'] // batch_size
            remaining_batch = af_item['quantity'] % batch_size
            for i in range(batches):
                v.append(Unit(
                    team=team,
                    type=af_type,
                    hp=air_force_data['classes'][af_type]['hp'],
                    ATK=air_force_data['classes'][af_type]['ATK'],
                    DEF=air_force_data['classes'][af_type]['DEF'],
                    cannot_attack=set(air_force_data['classes'][af_type]['cannot_attack']),
                    advantage_against=set(air_force_data['classes'][af_type]['advantage_against']),
                    game_scenario=game_scenario,
                    prob_hit=air_force_data['classes'][af_type]['prob_hit'],
                    condition_to_hit=air_force_condition,
                    multiple=batch_size
                ))
            if remaining_batch > 0:
                v.append(Unit(
                    team=team,
                    type=af_type,
                    hp=navy_data['classes'][af_type]['hp'],
                    ATK=navy_data['classes'][af_type]['ATK'],
                    DEF=navy_data['classes'][af_type]['DEF'],
                    cannot_attack=set(air_force_data['classes'][af_type]['cannot_attack']),
                    advantage_against=set(air_force_data['classes'][af_type]['advantage_against']),
                    game_scenario=game_scenario,
                    prob_hit=navy_data['classes'][af_type]['prob_hit'],
                    condition_to_hit=air_force_condition(af_type),
                    multiple=remaining_batch
                ))

    game_scenario.set_new_army_size(*team_quantities)

    return a_units, b_units, game_scenario

def calculate_unit_amount(unit_list):
    return sum([unit.multiple for unit in unit_list])

def check_stalemate(a_units, b_units):
    # O(n^2 worst)
    for a in a_units:
        for b in b_units:
            if a.can_attack(b) or b.can_attack(a):
                return False
    return True

def retreat(team, a_units, b_units, game_scenario, r, round_size, logger):
    if r < 0.2:
        did_retreat = True
        status = 'success'
    # With probability 0.25, takes a round of damage before exiting
    elif r < 0.3:
        did_retreat = True
        status = 'damaged'
        for i in range(round_size):
            a_unit = random.sample(a_units, 1)[0]
            b_unit = random.sample(b_units, 1)[0]
            if team == 1:
                a_unit.attack(b_unit)
            else:
                b_unit.attack(a_unit)
    # With probability 0.25, fails retreat
    else:
        did_retreat = False
        status = 'failure'
        # Gets half of the punishment
        for i in range(round_size, 2):
            a_unit = random.sample(a_units, 1)[0]
            b_unit = random.sample(b_units, 1)[0]
            if team == 1:
                a_unit.attack(b_unit)
            else:
                b_unit.attack(a_unit)


    logger.log_retreat(team, a_units, b_units, game_scenario, status)
    return did_retreat

def remove_dead(a_units, b_units):
    dead = []
    # Does not iterate destroying
    for unit in a_units:
        if unit.multiple < 0:
            raise Exception(str(unit) + ' has multiple < 0')
        if unit.is_dead():
            dead.append(unit)
    for unit in dead:
        a_units.remove(unit)
    dead = []
    for unit in b_units:
        if unit.multiple < 0:
            raise Exception(str(unit) + ' has multiple < 0')
        if unit.is_dead():
            dead.append(unit)
    for unit in dead:
        b_units.remove(unit)
    return a_units, b_units

def gameloop(a_units, b_units, game_scenario, round_size=50, log_file=None):
    """ main gameloop """
    from logger import Logger
    if log_file is None:
        from time import time
        log_file = 'logs/log_battle_' + str(int(time())) + '.txt'

    logger = Logger(log_file)
    logger.log_header()
    logger.log_initial_position(a_units, b_units, game_scenario)
    a_initial_troops = calculate_unit_amount(a_units)
    b_initial_troops = calculate_unit_amount(b_units)

    while True:
        # Increments game_scenario round
        game_scenario.incr_round()

        # 1. Remove dead
        a_units, b_units = remove_dead(a_units, b_units)

        # 2. Check dizimation
        if len(a_units) == 0:
            logger.log_final_position(a_units, b_units, game_scenario)
            print('b won!')
            print('b survived with', calculate_unit_amount(b_units), 'units')
            break
        if len(b_units) == 0:
            logger.log_final_position(a_units, b_units, game_scenario)
            print('a won!')
            print('a survived with', calculate_unit_amount(a_units), 'units')
            break

        # 3. Check retreat/POW
        a_unit_percentage = calculate_unit_amount(a_units) / a_initial_troops
        b_unit_percentage = calculate_unit_amount(b_units) / b_initial_troops
        if a_unit_percentage < 0.3 and (b_unit_percentage - a_unit_percentage) / (b_unit_percentage + a_unit_percentage) > 0.2:
            # With probability 0.4, retreats
            r = random.random()
            if r < 0.4:
                did_retreat = retreat(1, a_units, b_units, game_scenario, r, round_size, logger)
                if did_retreat:
                    logger.log_final_position(a_units, b_units, game_scenario)
                    break

        if b_unit_percentage < 0.3 and (a_unit_percentage - b_unit_percentage) / (b_unit_percentage + a_unit_percentage) > 0.2:
            r = random.random()
            if r < 0.4:
                did_retreat = retreat(2, a_units, b_units, game_scenario, r, round_size, logger)
                if did_retreat:
                    logger.log_final_position(a_units, b_units, game_scenario)
                    break


        # 4. Changes game scenario
        game_scenario.set_new_army_size(calculate_unit_amount(a_units), calculate_unit_amount(b_units))

        # 5. fights
        for i in range(round_size):
            a_unit = random.sample(a_units, 1)[0]
            b_unit = random.sample(b_units, 1)[0]
            if random.random() > 0.5:
                a_unit.attack(b_unit)
                b_unit.attack(a_unit)
            else:
                b_unit.attack(a_unit)
                a_unit.attack(b_unit)

        if check_stalemate(a_units, b_units):
            logger.log_stalemate(game_scenario)
            logger.log_final_position(a_units, b_units, game_scenario)
            break

# unit testing
if __name__ == '__main__':
    a_units, b_units, game_scenario = parse_battle_info()
    a_units, b_units = remove_dead(a_units, b_units)
    game_scenario.check()
    game_scenario.set_luck(10)
    gameloop(a_units, b_units, game_scenario, log_file='logs/unit_test.txt')
