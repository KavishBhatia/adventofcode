from get_data import get_data

data = get_data(day=4)

def p1(data):
    count = 0
    for x in data:
        x = x.replace('-',',').split(',')
        x = [int(n) for n in x]
        if ((x[0] - x[2]) * (x[1] - x[3])) <= 0:
            count+=1
        
    return count

def p2(data):
    count = 0
    for x in data:
        x = x.replace('-',',').split(',')
        x = [int(n) for n in x]
        if not set(range(x[0],x[1]+1)).isdisjoint(set(range(x[2],x[3]+1))):
            count+=1

    return count

print("part - 1", p1(data))
print("part - 2", p2(data))

def test_part1():
    assert p1(test_input) == 2

def test_part2():
    assert p2(test_input) == 4

test_input = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]