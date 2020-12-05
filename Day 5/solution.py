f = open("input.txt", "r")
ids = []

for line in f.readlines():
    binary = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    ids.append(int(binary, 2))

print("Part 1: ", max(ids))

ids = sorted(ids)
currentID = ids[0]

for i in ids:
    if i != currentID:
        print("Part 2: ", currentID)
        break
    currentID += 1