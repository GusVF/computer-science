# import math ------> this would substitute the "//" for "math.ceil" at line 15

# Tinta de 1 litro rende = 3 metros quadrados
# Tinta vendida em latas 18 litros
# Lata de tinta custa 80.00

# 30 metros / 3 = preciso de 10 litros //
# 10 litros / 18 que tem na lata = .055 //
# arredonda a quantidade para round.ceil.(quantidade) //
# retorna quantidade * custo de uma lata.


def paint_cost(wall_size: int, cost_per_can: int):
    paint_needed_in_litters = wall_size / 3
    total_paint_needed = paint_needed_in_litters // 18
    result = (total_paint_needed, total_paint_needed * cost_per_can)
    return result


result = paint_cost(120, 80)
print(result)
