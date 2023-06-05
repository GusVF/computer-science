from conta import Conta

# As duas versoes funcionam do mesmo jeito com pequenas diferencas
# class conta_investimento_2(Conta):
#     def __init__(self, numero, nome, saldo, taxaJuros):
#         Conta.__init__(self, numero, nome, saldo)
#         self.taxaJuros = taxaJuros


class conta_investimento(Conta):
    def __init__(self, numero, nome, saldo, taxaJuros):
        super().__init__(numero, nome, saldo)
        self.taxaJuros = taxaJuros

    def adiciona_juros(self):
        self.saldo += (self.saldo * self.taxaJuros / 100)
