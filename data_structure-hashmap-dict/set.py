# Dada um lista de numeros, retorne os numeros repetidos

def get_repeated(nums):
    seen_before = set()
    repeated = set()

    for n in nums:
        if n in seen_before:
            repeated.add(n)
        else:
            seen_before.add(n)

    return repeated


def get_seven(rolls):
    seen_before = set()
    lucky_rools = []
    for roll in rolls:
        if 7 - roll in seen_before:
            lucky_rools.append((7 - roll, roll))
            seen_before.discard(7 - roll)
        else:
            seen_before.add(roll)
    return lucky_rools


if __name__ == '__main__':
    nums = [1, 6, 3, 9, 6, 6, 3, -1, 4, 5, 7, 1]
    rolls = [5, 2, 1, 3, 2, 6, 1, 4, 2, 6, 3, 1, 1]

    # print(f'num: {get_repeated(nums)}')
    print(get_seven(rolls))
