from itertools import product
f = open("input.txt", "r")

grid = f.read().splitlines()

def get_online(dimensions):
    online = set()
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '#':
                online.add(tuple([i, j] + [0] * (dimensions - 2)))
    return online

def apply_rules(dimensions, cycles):
    online = get_online(dimensions)
    for _ in range(cycles):
        d = {}
        for pos in online:
            for neighbour in product([-1, 0, 1], repeat=dimensions):
                new = tuple(map(sum, zip(pos, neighbour)))
                if new != pos:
                    if new not in d.keys():
                        d[new] = 1
                    else:
                        d[new] += 1

        keepOnline = set([pos for pos in online if pos in d.keys() and d[pos] in [2, 3]])
        turnOn = set([pos for pos, numNeighbours in d.items() if pos not in online and numNeighbours == 3])
        online = keepOnline | turnOn
        
    return len(online)

print("Part 1: ", apply_rules(3, 6))
print("Part 2: ", apply_rules(4, 6))
