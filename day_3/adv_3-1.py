total = 0

with open("input_3", mode='r')as file:
    for line in file:
        mid = len(line) // 2
        l1, l2 = line[:mid], line[mid:]

        c = None
        for c1 in l1:
            for c2 in l2:
                if c1 == c2:
                    c = c1
                    break
            if c:
                break
        
        if c.islower():
            total += ord(c) - 96
        else:
            total += ord(c) - 38

print(total)