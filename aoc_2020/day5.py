def get_seat_id(seat_string):
    row_start = 0
    row_length = 128
    column_start = 0
    column_length = 8
    for i in seat_string:
        if i == 'F':
            row_length = row_length / 2
        elif i == 'B':
            row_length = row_length / 2
            row_start = row_start + (row_length)
        elif i == 'L':
            column_length = column_length / 2
        elif i == 'R':
            column_length = column_length / 2
            column_start = column_start + (column_length)

    return int(row_start) * 8 + int(column_start)


def get_data(filepath):
    file = open(filepath, 'r')
    lines = file.read().splitlines()
    return lines


def find_max(filepath):
    data = get_data(filepath)
    ids = []
    for i in data:
        ids.append(get_seat_id(i))
    return max(ids)


def find_missing(filepath):
    data = get_data(filepath)
    ids = []
    for i in data:
        ids.append(get_seat_id(i))
    missing = list(set(list(range(63, 936))) - set(ids))
    return missing[0]


print((find_max('aoc_2020/data/day5_data.txt')))
print((find_missing('aoc_2020/data/day5_data.txt')))
