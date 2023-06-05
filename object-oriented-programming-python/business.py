from employees import Employees


class Business:
    func = []

    def __init__(self):
        print("Empresa ficticia em funcionamento!")

    def funcionar(self):
        while True:
            print("1. Contratar")
            print("2. Exibir lista de funcionarios!")
            op = int(input())

            if op == 1:
                self.contratar()
            elif op == 2:
                self.exibir()
            else:
                print("Opcao invalida!")

    def contratar(self):
        name = input('nome: ')
        self.func.append(Employees(name))

    def exibir(self):
        for employee in self.func:
            print(employee.returnName())


business = Business()
business.funcionar()
