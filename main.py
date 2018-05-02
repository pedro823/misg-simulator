from gameloop import gameloop, parse_battle_info

def main():
    print('-' * 40)
    print('SIMULADOR DE GUERRA MISG 2018')
    print('-' * 40)
    file_name = input('Arquivo para ser lido (battle_info/battle_info.json):')
    if file_name == ''
        file_name = 'battle_info/battle_info.json'
    luck_factor = float(input('Fator de sorte: '))
    a_units, b_units, game_scenario = parse_battle_info(file_name, luck_factor)
    gameloop()

if __name__ == '__main__':
    main()
