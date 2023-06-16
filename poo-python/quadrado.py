from figura_geometrica import FiguraGeometrica


class Quadrado(FiguraGeometrica):
    def __init__(self, side: int):
        self.side = side

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado
