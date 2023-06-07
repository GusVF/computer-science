# Em um jogo de baralho, as cartas estão representadas por um array numérico.
# Para iniciar o jogo, devemos embaralhar as cartas.
# Faremos isto dividindo uma porção de cartas em 2 e depois mesclando as duas.

# Exemplo 1:
# cartas = [2, 6, 4, 5]
# cartas por parte = 2
# resultado = [2, 4, 6, 5]

# Exemplo 2:
cartas = [1, 4, 4, 7, 6, 6]
# cartas por parte = 3
# resultado = [1, 7, 4, 6, 4, 6]


def card_shuffle(cards: list):
    shuffled = []
    split_deck = len(cards) // 2
    for off_set in range(split_deck):

        shuffled.extend(cards[off_set::split_deck])
    return shuffled


result = card_shuffle(cartas)
print('Not shuffled', cartas)
print('Shuffled', result)
# test = cartas[:len(cartas) // 2]
# print(test)
