class Pet():
    def __init__(self, nome, especie, idade, humano_pai):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.humano_pai = humano_pai

    def __str__(self):
        return f"""
        -Especie do Pet: {self.especie}
        -Nome do Pet: {self.nome}
        -Idade do Pet: {self.idade}
        -humano_pai: {self.humano_pai}
        """


molly = Pet('Molly', 'Shitzu', 6, 'Gustavo')

print(molly)
