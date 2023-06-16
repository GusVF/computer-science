from figura_geometrica import FiguraGeometrica


class Retangulo(FiguraGeometrica):
    def __init__(self, base: int, hight: int):
        self.base = base
        self.hight = hight

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
