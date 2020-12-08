def get_data(filepath):
    file = open(filepath, 'r')
    lines = file.read().split('\n\n')
    return lines


def get_unique(filepath):
    data = get_data(filepath)
    new_lines = []
    for i in data:
        new_string = "".join(i.splitlines())
        new_lines.append(new_string)
    count = 0
    for i in new_lines:
        count += len(set(list(i)))
    return count


def get_unique_2(filepath):
    data = get_data(filepath)
    ct = 0
    for group in data:
        num_ppl = len(group.split())
        unique = list(set(group))
        if '\n' in unique:
            unique.remove('\n')
        for letter in unique:
            if group.count(letter) == num_ppl:
                ct += 1
    return ct


print(get_unique_2('aoc_2020/data/day6_data.txt'))
