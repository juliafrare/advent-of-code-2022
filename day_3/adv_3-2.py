total = 0

with open("input_3", mode='r')as file:
    trio = []
    for line in file:
        trio.append(line)

        if len(trio) == 3:
            c = None
            common = []
            
            for c1 in trio[0]:
                for c2 in trio[1]:
                    if c1 == c2:
                        common.append(c1)
                        break

            for c1 in common:
                for c2 in trio[2]:
                    if c1 == c2:
                        c = c1
                        break
                if c:
                    break

            if c.islower():
                total += ord(c) - 96
            else:
                total += ord(c) - 38
            
            trio.clear()

print(total)