theirs = {'A': 1, 'B': 2, 'C': 3}
mine = {'X': 1, 'Y': 2, 'Z': 3}

total = 0

with open("input", mode='r')as file:
    for line in file:
        t, m = line.split()

        total += mine[m]

        if theirs[t] == mine[m]:
            total += 3
        elif (theirs[t] == mine[m] - 1) or (theirs[t] == mine[m] + 2):
            total += 6

print(total)