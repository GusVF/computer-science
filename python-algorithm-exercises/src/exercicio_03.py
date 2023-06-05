def square(n: int):
    for row in range(n):
        return n * '*'


square(4)
# print(square)
# Some os inteiros anteriores de um número

# exercicio extra usado na aula


def sum_to(n: int) -> int:
    if n == 0:
        return 0

    return n + sum_to(n - 1)


if __name__ == "__main__":
    # 4 + 3 + 2 + 1 + 0 = 10
    sum_to(5)

obj1 = {
  'name': 'Rogerinho'
}

obj2 = {
  'name': 'Rogerinho'
}

obj3 = obj1
a = 'Rogerinho'
b = 'Rogerinho'

print(a == b)  # True
print(obj1 == obj2)  # True
print(obj1 is obj2)  # False
print(obj1 is obj3)  # True
