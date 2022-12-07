with open("files/input_day2.txt", "r") as f:
    lines = f.read()

inputs = [i.split(' ') for i in lines.split('\n')]

rps = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

def p1(inputs):

    win_comb = [['A','Y'], ['B','Z'], ['C','X']]
    score = 0
    for input in inputs:
        score += rps.get(input[1])
        if input in win_comb:
            score += 6
        elif rps.get(input[0]) == rps.get(input[1]):
            score += 3
    return score

def p2(inputs):

    lose_comb = {
    'B':'A',
    'C':'B',
    'A':'C'
    }

    win_comb = {
        'A':'B',
        'B':'C',
        'C':'A'
    }

    score = 0
    for input in inputs:
        if input[1] == 'X':
            score += rps.get(lose_comb.get(input[0]))
        elif input[1] == 'Y':
            score += 3
            score += rps.get(input[0])
        elif input[1] == 'Z':
            score += 6
            score += rps.get(win_comb.get(input[0]))

    return score


print("Part 1 - ",p1(inputs))
print("Part 2 - ",p2(inputs))


test_input = [['A', 'Y'],['B','X'],['C','Z']]

def test_part1():
    assert p1(test_input) == 15

def test_part2():
    assert p2(test_input) == 12


