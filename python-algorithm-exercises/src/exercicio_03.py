def square(n: int):
    for row in range(n):
        print(n * '*')


square(4)

# Some os inteiros anteriores de um número

# exercicio extra usado na aula


def sum_to(n: int) -> int:
    if n == 0:
        return 0

    return n + sum_to(n - 1)


if __name__ == "__main__":
    # 4 + 3 + 2 + 1 + 0 = 10
    print(sum_to(5))
