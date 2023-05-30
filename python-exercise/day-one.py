from collections import Counter
import random

# counter = 10
# counter += 1
# counter = counter + 10
# counter = counter / 2
# counter -= 10

# find = 18 > counter < 8
# print('counter is smaller then 18 and bigger then 08', counter, find)

# evenNumbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# oddNumbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# evenNumbers.extend(oddNumbers)
# evenNumbers.insert(evenNumbers[-1], 30)
# evenNumbers.insert(evenNumbers[-1], 40)
# evenNumbers.reverse()
# evenNumbers.sort()

# trybe_course = ["Introdução", "Front-end", "Back-end"]
# trybe_course.append('Ciência da Computação')
# trybe_course.remove('Introdução')
# trybe_course.insert(0, 'Fundamentos')
# print(trybe_course)

# user = ('Gustavo', 'Ferreira', 46)
# print(user[1])

# permissions = {"member", "group"}
# permissions.add('affiliate')
# permissions.add('user')
# permissions.union({'user'})

# languages = ['Python', 'Java', 'JavaScript']
# print(languages)
# enumerate_prime = enumerate(languages)
# print(list(enumerate_prime))
# for index, language in enumerate(languages):
# print(f'{index} - {language}')

# n = 10
# last, next = 0, 1
# while last < n:
#     print(last)
#     last, next = next, last + next

# number = 5
# result = 1

# for factor in range(1, number+1):
#     result *= factor
# result
# print(result)

# ratings = [6, 8, 5, 9, 10, 12, 16, 19, 22, 24, 27, 29, 32]
# new_rating = [10 * rating for rating in ratings]

# identation matters. The print idented and commented
# returns each run of the 'for' while the other print returns just the
# result because it prints only after it finishes the for loop.
# for rating in ratings:
#     new_rating.append(rating * 10)
# print(new_rating)

# for rating in ratings:
#     if (rating % 3) == 0:
# print(f'{rating}, e multiplo de 3!')


# def imc(peso, altura):
#     result = peso / (altura / 100) ** 2
#     print(result)


# imc(90, 165)

# frase = 'Vou continuar a estudar programacao e vou conseguir um otimo emprego!'
# vogais = 'aeiou'
# lista_vogais = []
# lista_consoantes = []

# for letra in frase:
#     if letra in vogais:
#         lista_vogais.append(letra)
#     if letra not in vogais:
#         lista_consoantes.append(letra)
# print(lista_vogais)
# print(lista_consoantes)

# lista_v = [letra for letra in frase if letra in vogais]
# lista_c = [
#     letra
#     for letra in frase
#     if letra not in vogais]
# set_v = {letra for letra in frase if letra in vogais}
# set_c = {letra for letra in frase if letra not in vogais}
# print(lista_v)
# print(lista_c)
# set_v = list(set_v)
# set_v.sort()
# print(set_v)
# set_c = list(set_c)
# set_c.sort()
# set_c.remove(' ')
# set_c.remove('!')
# print(set_c)

# ratings = [6, 8, 5, 9, 10, 12, 16, 19, 22, 24, 27, 29, 32]
# for index, number in enumerate(ratings):
#     print(index, number)
# print(number)

# random_list = random.sample(range(0, 100000), random.randint(50, 5000))
# random_list.sort()
# enumerate(random_list)
# print(random_list)
# print(len(random_list))

lista_de_numeros = []

# for x in range(1000):
#     lista_de_numeros.append(random.randint(0, 1000))
# print(lista_de_numeros, 'lista de numeros')
# print(lista_de_numeros)
# counter = Counter(lista_de_numeros)
# most_common = counter.most_common()
# elemento_comum, numero_de_vezes = most_common[0]
# print(most_common)
# print(
#     f'Elementto mais comum: {elemento_comum}, '
#     f'aparecendo: {numero_de_vezes} vezes.'
# )
