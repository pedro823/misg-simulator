from unit import Unit
from game_scenario import GameScenario
import json

with open('troop_info/army.json', 'r') as f:
    data = json.load(f)

game_scenario = GameScenario(a_army_size=1, b_army_size=1, luck=0)

a = Unit(team=1,
         type='A',
         hp=data['classes']['A']['hp'],
         ATK=data['classes']['A']['ATK'],
         DEF=data['classes']['A']['DEF'],
         game_scenario = game_scenario,
         prob_hit=0.8)
b = Unit(team=1,
         type='B',
         hp=data['classes']['B']['hp'],
         ATK=data['classes']['B']['ATK'],
         DEF=data['classes']['B']['DEF'],
         game_scenario = game_scenario,
         multiple=3)

while True:
    if a.is_dead():
        print("B vence!")
        print(b.multiple)
        break
    a.attack(b)
    if b.is_dead():
        print("A vence!")
        print(a.multiple)
        break
    b.attack(a)
