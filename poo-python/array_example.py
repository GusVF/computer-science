import sys
"""Perceba que temos uma coleção de valores
e operações que atuam sobre estes valores,
de acordo com o que foi definido pelo TAD."""


class ListaArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        # quando pedido o tamanho do array
        # retorne o tamanho de data
        return len(self.data)

    def __str__(self):
        # converte para string e exibe os valores de data
        return str(self.data)

    def get(self, index):
        # recupera o elemento no índice informado
        return self.data[index]

    def set(self, index, value):
        # insere um elemento no índice informado
        self.data.insert(index, value)

    def update(self, index, value):
        self.data[index] = value


# vamos inicializar e preencher uma estrutura de dados array
array = ListaArray()
# array.set(0, "Felipe")
# array.set(1, "Ana")
# array.set(2, "Shirley")
# array.set(3, "Miguel")
# array.set(4, "Marcos")
# array.set(5, "Patrícia")
# sys.getsizeof retorna o tamanho da lista em bytes
array_memory_size = sys.getsizeof(array.data)
# print(array_memory_size)

# ...
# array = ListaArray()

array.set(0, "Marcos")
array.set(1, "Patrícia")
# print(array), internamente chama o método array.__str__() que implementamos
# print(array)  # saída: ["Marcos", "Patrícia"]

# inserindo no começo do array
array.set(0, "Valeria")
# print(array)  # saída: ["Valeria", "Marcos", "Patrícia"]
array.set(1, "Miguel")
array.update(1, "Thaina")
# inserindo em uma posição intermediária
# print(array)  # saída: ['Valeria', 'Miguel', 'Marcos', 'Patrícia']


# print("-----")

# podemos iterar sobre seus elementos da seguinte maneira
index = 0
# enquanto há elementos no array
while index < len(array):
    # recupera o elemento através de um índice
    # print("Index:", index, ", Nome:", array.get(index))
    index += 1
