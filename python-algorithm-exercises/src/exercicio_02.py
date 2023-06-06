def total_list_items(list_arr: list):
    result = 0
    for number in list_arr:
        result += number
    return result


total = total_list_items([2, 3, 4, 1])
print(total)
