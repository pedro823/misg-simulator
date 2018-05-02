from gameloop import gameloop, parse_battle_info
from util import is_windows, unix_to_nt

def main():
    print('-' * 40)
    print('SIMULADOR DE GUERRA MISG 2018')
    print('-' * 40)
    file_name = input('Arquivo para ser lido (battle_info/battle_info.json):')
    if file_name == '':
        file_name = 'battle_info/battle_info.json'
        if is_windows():
            file_name = unix_to_nt(file_name)
    try:
        luck_factor = float(input('Fator de sorte (0): '))
    except ValueError:
        luck_factor = 0
    a_units, b_units, game_scenario = parse_battle_info(file_name, luck_factor)
    gameloop(a_units, b_units, game_scenario)

if __name__ == '__main__':
    main()
