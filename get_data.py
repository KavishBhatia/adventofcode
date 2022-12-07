def get_data(day):
    path = "files/input_day"+str(day)+".txt"
    with open(path, "r") as f:
        lines = f.read()
    return lines.split('\n')