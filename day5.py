from get_data import get_data
from math import floor
from collections import defaultdict


data = get_data(day=5)

def process_data(data):
    crates = []
    moves = []
    for x in data:
        if not x.startswith('move') and x != '':
            crates.append(x)
        if x.startswith('move'):
            moves.append(x)

    crates_dict = defaultdict(list)

    for c in crates:
        for i, l in enumerate(c):
            if l.isupper():
                k = floor(i/3)
                if k <=5:
                    crates_dict[k].append(l)
                elif k > 5 and k <= 9 :
                    crates_dict[k-1].append(l)
                elif k>9:
                    crates_dict[k-2].append(l)
                    
    crates_dict[2] = crates_dict[1]
    del crates_dict[1]
    crates_dict[1] = crates_dict[0]
    del crates_dict[0]

    crates_stack = list()
    for i in range(1, len(crates_dict)+1):
        crates_stack.append(crates_dict[i][::-1])

    moves = [ x.split(' ') for x in moves]

    return crates_stack, moves

    
def p1(data):
    crates_stack, moves = process_data(data)
    for item in moves:
        for i in range(0, int(item[1])):
            move_crate = crates_stack[int(item[3])-1].pop()
            crates_stack[int(item[5])-1].append(move_crate)

    for crate in crates_stack:
        print(crate[-1], end="")
    print()

def p2(data):
    crates_stack, moves = process_data(data)
    for item in moves:
        move = int(item[1])
        move = move*-1
        crates_stack[int(item[3])-1], temp =  crates_stack[int(item[3])-1][:move], crates_stack[int(item[3])-1][move:]
        for _ in range(len(temp)):
            crates_stack[int(item[5])-1].append(temp.pop(0))

    for crate in crates_stack:
        print(crate[-1], end="")
    print()

p1(data)
p2(data)