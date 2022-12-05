with open("files/input_day1.txt", "r") as f:
    inp = f.readlines()

temp = []
inps = []

for i in inp:
    element = i.rstrip("\n")
    if len(element) > 0:
        temp.append(int(element))
    elif len(element) == 0:
        inps.append(sum(temp))
        temp = []

inps.sort(reverse=True)
print("Part 1 - ", inps[0])
print("Part 2 - ", sum(inps[:3]))