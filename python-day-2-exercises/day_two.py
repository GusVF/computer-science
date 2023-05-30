# from functools import partial
# import random
# import time

# def soma(x, y): return x + y


# increment = partial(soma, 3)

# print(increment(7))


# array = []
# for i in range(21):
#     array.append(random.randint(1, 100))
# print(array)

new_array = [
    25,
    74,
    76,
    71,
    55,
    52,
    42,
    50,
    40,
    24,
    1,
    7,
    19,
    64,
    38,
    56,
    29,
    86,
    91,
    23,
    87,
]
# print(new_array)


# def squared_array(numbers: set[int]):
#     array = []
#     for number in numbers:
#         array.append(number ** 2)
#     # array.sort()
#     # print(array)
#     return array


# squared_array(new_array)


# def random_list():
#     array = []
#     for _ in range(20):
#         number = random.randint(0, 100)
#         array.append(number)
#     return array


# new_random_array = random_list()
# print(new_random_array)


# def multiply_arrays(array1, array2):
#     result = []
#     number_of_iterations = 0

#     for number1 in array1:
#         print(f'Array 1: {number1}')
#         for number2 in array2:
#             print(f'Array 2: {number2}')
#             result.append(number1 * number2)
#             number_of_iterations += 1

#     print(f'{number_of_iterations} iterações!')
#     return result


# meu_array = [25, 74, 76, 71, 55, 52, 42, 50, 40, 24]

# multiply_arrays(meu_array, meu_array)


# A estrutura deve estar ordenada para que a busca binária funcione
def binary_search(numbers, target):
    # definir os índices
    start = 0
    end = len(numbers) - 1

    while start <= end:  # os índices podem ser no máximo iguais,
        # o início não pode ultrapassar o fim
        mid = (start + end) // 2  # encontro o meio

        if (
            numbers[mid] == target
        ):  # se o elemento do meio for o alvo, devolve a posição do meio
            return mid

        if (
            target < numbers[mid]
        ):  # se o elemento for menor, atualiza o índice do fim
            end = mid - 1
        else:  # caso contrário, atualiza o índice do inicio
            start = mid + 1

    return -1  # Não encontrou? Retorna -1


numbers = [2, 3, 4, 10, 42, 11, 15, 40]
target = 40

result = binary_search(numbers, target)
# print(f"Elemento encontrado na posição: {result}")


def calculations(n):
    number1 = 0
    for n1 in range(n):
        number1 += n1

    number2 = 0
    for n1 in range(n):
        for n2 in range(n):
            number2 += n1 + n2

    number3 = 0
    for n1 in range(n):
        for n2 in range(n):
            for n3 in range(n):
                number3 += n1 + n2 + n3

    return number1, number2, number3


# n1, n2, n3 = calculations(100)
# print(f'{n1}, {n2}, {n3}')

# def count_down(number: int):
#     if number > 100:
#         print('Finished')
#     else:
#         print(number)
#         # time.sleep(1)
#         count_down(number + 1)


# count_down(1)

# def saudacao():
#     print("Oi")


# def despedida():
#     print("Tchau")


# def init():
#     print("Inicio")
#     saudacao()
#     print("Fim")
#     despedida()


# init()


# def sum_of_all(n: int):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         return n + sum_of_all(n - 1)


# sum_of_all(4)


def fibonacci(num):  # nome da função e parâmetro
    if num <= 1:  # condição de parada
        return num
    else:
        # print(num)
        # chamada de si mesma com um novo valor
        return fibonacci(num - 2) + fibonacci(num - 1)


result = fibonacci(10)
print(result)
