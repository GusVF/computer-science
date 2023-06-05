numbers = [1, 7, 5, 3, 9, 2, 6, 8, 4]


def selection_sort(numbers):
    n = len(numbers)
    for index in range(n - 1):
        min_element_index = index
        for search_index in range(index + 1, n):
            # print(search_index, 'search index')
            # print(numbers[search_index], 'n')
            if numbers[search_index] < numbers[min_element_index]:
                min_element_index = search_index
        # Troca os elementos de posição
        current_element = numbers[index]
        # print(numbers[index])
        numbers[index] = numbers[min_element_index]
        # print(numbers[index])
        numbers[min_element_index] = current_element
        # print(numbers[index])
    return numbers


# print(f"Lista inicial: {numbers}")
# ordered_numbers = selection_sort(numbers)
# print(f"Lista final: {ordered_numbers}")


def sort_number(number_list: list):
    # Modify the original in place and returns it
    number_list.sort()
    return number_list


def sort_number1(number_list1: list):
    # sorts the list without modifying the original list
    return sorted(number_list1)


result = sort_number(numbers)
result1 = sort_number1(numbers)
# sum = result == result1
# print(result)
# print(numbers)
# print(result1)
# print(sum)

n1 = 3
n2 = 3
n3 = n1 == n2
n4 = n1
n5 = n2 == n4
# print(n5)

array = [
    "Lucas",
    "Nádia",
    "Fernanda",
    "Cairo",
    "Joana",
    "Gustavo",
    "Alcantara",
    "Sophia",
    "Gabriel",
    "Isabella",
    "Enzo",
    "Laura",
    "Pedro",
    "Julia",
    "Mateus",
    "Valentina",
    "Lucca",
    "Manuela",
    "Davi",
    "Alice",
    "Arthur",
    "Heloisa",
    "Miguel",
    "LaraCroft"
]

# Finds by longest name


def longest_name(names: list):
    bigger_name = names[0]
    # print(bigger_name)
    for name in names:
        if len(name) > len(bigger_name):
            bigger_name = name
    return bigger_name


result = longest_name(array)
# print(result)

# Finds by first letter


def names_with_f(names: list[int], letter: int):
    letter.lower()
    name_with_letter = []
    for name in names:
        if name[0] == letter:
            name_with_letter.append(name)

    return name_with_letter


result = names_with_f(array, 'L')
print(result)
