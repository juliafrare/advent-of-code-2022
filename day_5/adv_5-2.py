stacks = [[] for i in range(9)]

def add_to_stack(crate, stack):
    if crate != "   ":
        stacks[stack].insert(0, crate)

with open("input_5", mode='r')as file:
    i = 0
    for line in file:
        if i < 8:
            for j in range(9):
                add_to_stack(line[4*j:4*(j+1)-1], j)
        if i >= 10:
            _, n_move, _, st_1, _, st_2 = line.split(" ")
            for j in range(int(n_move), 0, -1):
                crate = stacks[int(st_1) - 1].pop(-j)
                stacks[int(st_2) - 1].append(crate)
        i += 1

for i in range(9):
    print(stacks[i][-1])