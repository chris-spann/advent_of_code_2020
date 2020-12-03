import math


def get_data(filepath):
    file = open(filepath, 'r')
    lines = file.read().splitlines()
    return lines


def traverse(filepath, x_incr, y_incr):
    data = get_data(filepath)
    length = len(data)
    width = len(data[0])
    tree_ct = 0
    x_pos = 0
    y_pos = 0
    while y_pos < length:
        if data[y_pos][x_pos % width] == '#':
            tree_ct += 1
        y_pos += y_incr
        x_pos += x_incr
    return tree_ct


def get_product():
    res = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        res.append(traverse('aoc_2020/data/day3_data.txt', slope[0], slope[1]))
    return math.prod(res)


print(get_product())
