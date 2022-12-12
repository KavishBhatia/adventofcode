from get_data import get_data

data = get_data(day=6)


def p1_p2(data, window_size=4):
    for text in data:
        pos = 0
        for i in range(0, len(text) - window_size):
            window = text[i : i + window_size]
            if len(set(window)) == window_size:
                pos = i + window_size
                break
        return pos   

print("Part - 1", p1_p2(data, window_size=4))
print("Part - 2", p1_p2(data, window_size=14))