# parametros serao 3 medidas de lados de triangulo
# identificar o maior lado e verificar se os outros dois somados sao maiores
# verificar se tem 3 lados iguais
# verificar se tem 2 lados iguais
# verificar se tem 3 lados diferentes
def trybeangle_type(side1, side2, side3):
    is_triangle = (
        side1 + side2 > side3 and
        side2 + side3 > side1 and
        side3 + side1 > side2
    )
    if not is_triangle:
        return "Not a triangle"
    elif side1 == side2 == side3:
        return "equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isósceles"
    else:
        return "escaleno"


result = trybeangle_type(8, 8, 8)
print(result)
