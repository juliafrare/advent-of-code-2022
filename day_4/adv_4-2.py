total = 0

with open("input_4", mode='r')as file:
    for line in file:
        s1, s2 = line.split(',')

        x1, y1 = s1.split('-')
        x2, y2 = s2.split('-')
        #if x1 <= x2 <= y1 or x1 <= y2 <= y2
        if (int(x1) <= int(x2) and int(x2) <= int(y1)) or (int(x1) <= int(y2) and int(y2) <= int(y1)):
            total += 1
        elif (int(x2) <= int(x1) and int(x1) <= int(y2)) or (int(x2) <= int(y1) and int(y1) <= int(y2)):
            total += 1

print(total)