from collections import Counter
import math
import random


class Statistics:
    def __init__(self, numbers):
        self.numbers = numbers

    def media(self):
        return sum(self.numbers) / len(self.numbers)

    def mediana(self):
        numbers = sorted(self.numbers)
        index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (numbers[index - 1] + numbers[index]) / 2

        return numbers[index]

    def moda(self):
        number, _ = Counter(self.numbers).most_common()[0]
        return number


array = [
          82, 37, 4, 42, 33, 71, 94, 77, 16, 55, 22, 55, 31, 27, 78, 75, 70,
          5, 89, 11, 75, 51, 36, 83, 88, 52, 34, 7, 73, 50, 13, 50, 80, 96,
          62, 44, 56, 20, 9, 21, 32, 14, 70, 24, 27, 73, 3, 84, 4, 14
            ]

statistics = Statistics(array)
mean = statistics.media()
mediana = statistics.mediana()
moda = statistics.moda()
print('Mean', mean)
print('Mediana', mediana)
print('Moda', moda)


numbers = []
for _ in range(50):
    num = math.floor(random.random() * 100)
    numbers.append(num)

# print(numbers)
