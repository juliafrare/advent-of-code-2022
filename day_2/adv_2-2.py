guide = {'A': 1, 'B': 2, 'C': 3}

total = 0

with open("input_2", mode='r')as file:
    for line in file:
        t, r = line.split()

        if r == 'X':
            total += guide[t] - 1 if t != 'A' else 3
        elif r == 'Y':
            total += 3 + guide[t]
        else:
            total += 7 + guide[t] if t != 'C' else 7

print(total)