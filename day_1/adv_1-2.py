elves = []

with open("adv_1.txt", mode="r") as file:
    calories = 0
    for line in file:
        if line[:-1].isalnum():
            calories += int(line[:-1])
        else:
            elves.append(calories)
            calories = 0

elves.sort()

largest = elves[-3:]
'''
for e in elves:
    if e > largest[0]:
        largest[0] = e
    elif e > largest[1]:
        largest[1] = e
    elif e > largest[2]:
        largest[2] = e
'''

print(sum(largest))