def get_data(filepath):
    file = open(filepath, 'r')
    lines = file.read().split('\n\n')
    return lines


def is_valid(str):
    fields = str.split()
    pass_dict = {}
    for field in fields:
        pass_dict[field.split(':')[0]] = field.split(':')[1]
    return pass_dict.keys() >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def is_valid_2(str):
    fields = str.split()
    pass_dict = {}
    hex_chars = '1234567890abcdef'
    for field in fields:
        pass_dict[field.split(':')[0]] = field.split(':')[1]
    if pass_dict.keys() >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}:
        if 1920 <= int(pass_dict['byr']) <= 2002:
            if 2010 <= int(pass_dict['iyr']) <= 2020:
                if 2020 <= int(pass_dict['eyr']) <= 2030:
                    if pass_dict['pid'].isdigit() and len(pass_dict['pid']) == 9:
                        if pass_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            if pass_dict['hcl'][0] == '#' and len(pass_dict['hcl'][1:]) == 6:
                                if len(set(pass_dict['hcl'][1:] + hex_chars)) == 16:
                                    if pass_dict['hgt'][-2:].lower() == 'in':
                                        if 59 <= int(pass_dict['hgt'][:-2]) <= 76:
                                            return True
                                    elif pass_dict['hgt'][-2:].lower() == 'cm':
                                        if 150 <= int(pass_dict['hgt'][:-2]) <= 193:
                                            return True
    return False


def process_data(filepath):
    data = get_data(filepath)
    valid_ct = 0
    for i in data:
        if is_valid_2(i) is True:
            valid_ct += 1
    return valid_ct


print(process_data('aoc_2020/data/day4_data.txt'))
