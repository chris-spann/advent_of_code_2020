
def validate(str):
    split = str.split(' ')
    min = int(split[0].split('-')[0])
    max = int(split[0].split('-')[1])
    req = split[1][0]
    pswrd = split[2]
    if pswrd.count(req) >= min:
        if pswrd.count(req) <= max:
            return 'valid'
    return 'invalid'


def validate_part2(str):
    split = str.split(' ')
    pos_1 = int(split[0].split('-')[0]) - 1
    pos_2 = int(split[0].split('-')[1]) - 1
    req = split[1][0]
    pswrd = split[2]
    if pswrd[pos_1] == req and pswrd[pos_2] != req:
        return 'valid'
    if pswrd[pos_1] != req and pswrd[pos_2] == req:
        return 'valid'
    return 'invalid'


def get_data(filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    return lines


def process_data(filepath):
    data = get_data(filepath)
    results = []
    for line in data:
        results.append(validate_part2(line))
    return results.count('valid')


print(process_data('aoc_2020/data/day2_data.txt'))
