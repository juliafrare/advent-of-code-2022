elves = []

with open("input_1", mode="r") as file:
    calories = 0
    for line in file:
        if line[:-1].isalnum():
            calories += int(line[:-1])
        else:
            elves.append(calories)
            calories = 0

elves.sort()

largest = elves[-3:]

print(sum(largest))