from figura_geometrica import FiguraGeometrica
from math import pi as PI


class circulo(FiguraGeometrica):
    def __init__(self, raio: int):
        self.raio = raio

    def area(self):
        return PI * self.raio * self.raio

    def perimetro(self):
        return 2 * PI * self.raio
