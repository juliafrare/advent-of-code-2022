total = 0

with open("input_4", mode='r')as file:
    for line in file:
        s1, s2 = line.split(',')

        x1, y1 = s1.split('-')
        x2, y2 = s2.split('-')
        if int(x1) <= int(x2) and int(y1) >= int(y2):
            total += 1
        elif int(x1) >= int(x2) and int(y1) <= int(y2):
            total += 1

print(total)