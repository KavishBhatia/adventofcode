def get_data(filename):
    with open(filename, "r") as f:
        lines = f.read()
    return lines.split('\n')

filename = "files/input_day3.txt"
data = get_data(filename)

def calc_prior(char):
    
    if char.islower():
        return ord(char) - 96
    elif char.isupper():
        return ord(char.lower()) - 70 #(96 - 26)
    
def p1(inputs):
    priorities = 0
    for s in inputs:
        a,b = s[:len(s)//2], s[len(s)//2:]
        common_char = set(a).intersection(set(b)).pop()
        priorities += calc_prior(common_char)

    return priorities

def p2(inputs):
    priorities = 0
    for idx in range(0, len(inputs), 3):
        group = inputs[idx:idx+3]
        common_char = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        priorities += calc_prior(common_char)
    return priorities

def test_part1():
    assert p1(test_input) == 157

def test_part1():
    assert p2(test_input) == 70

test_input = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw'
]

print("Part - 1", p1(data))
print("Part - 2", p2(data))