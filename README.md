### Simulador de guerra do MISG ###

Feito por: github.com/pedro823

#### Como editar os dados da batalha ####
Para isso, edite o arquivo battle_info/battle_info.json.
O arquivo está no formato [JSON](https://pt.wikipedia.org/wiki/JSON).

Um exemplo de JSON válido para o battle_info:
```json
[
  {
    "team": 1,
    "army": [
      {
        "unit_type": "elite",
        "quantity": 10
      },
      {
        "unit_type": "A",
        "quantity": 50
      }
    ],
    "navy": [
    ],
    "air_force": [
      {        
        "unit_type": "plane",
        "quantity": 1
      }
    ]
  },
  {
    "team": 2,
    "army": [
      {
        "unit_type": "B",
        "quantity": 100
      }
    ],
    "navy": [
    ],
    "air_force": [
      {        
        "unit_type": "zeppelin",
        "quantity": 2
      }
    ]
  }
]
```

Versão com comentários, explicando cada um deles:

```js
[
  {
    "team": 1, // Descreve o time 1
    "army": [ // Descreve todo o exército do time 1
      { // primeiro objeto do exército
        "unit_type": "elite", // descreve que esse objeto contém 10 elites
        "quantity": 10
      },
      { // segundo objeto do exército
        "unit_type": "A", // Todos os tipos de unidades podem ser vistos no arquivo troop_info/army.json
        "quantity": 50
      } // note a ausência da vírgula no último item
    ],
    "navy": [ // Descreve toda a marinha do time 1
      // Vazio! nenhuma marinha nessa batalha
    ],
    "air_force": [ // Descreve toda a força aérea do time 1
      { // primeiro objeto da força aérea
        "unit_type": "plane", // descreve que há um avião
        "quantity": 1
      }
    ] // lembre de por unidades no local certo! nada de "plane" na marinha.
  },
  {
    "team": 2, // Descreve o time 2
    "army": [ // Descreve todo o exército do time 2
      { // primeiro objeto do exército
        "unit_type": "B", // Descreve que há 100 unidades do B
        "quantity": 100
      }
    ],
    "navy": [
    ],
    "air_force": [
      { // Lembre de por a chave toda vez que for colocar um ITEM na LISTA. Um ITEM é tudo dentro de uma chave.
        "unit_type": "zeppelin", // 2 zeppelins
        "quantity": 2
      }
    ]
  }
]
```

#### Para rodar o programa ####
É necessário ter [Python 3](https://www.python.org/downloads/)
instalado. Qualquer versão acima de 3 deve funcionar. Foi programado
e testado em Python 3.6.4.

Para rodar no Linux: em um terminal, entre na pasta e digite

    $ python3 main.py

Para rodar no Windows: em um terminal, entre na pasta e digite

    > main.py
