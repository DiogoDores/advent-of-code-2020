from collections import defaultdict
f = open("input.txt", "r")

paths = [x for x in f.read().split()]
tiles = defaultdict(tuple)


for path in paths:
    pos = [0, 0]
    i = 0
    while i != len(path):
        if path[i] == 'e':
            pos[0] += 1
        elif path[i] == 'w':
            pos[0] -= 1
        elif path[i] == 'n':
            if path[i + 1] == 'e':
                pos[1] += 1
            elif path[i + 1] == 'w':
                pos[0] -= 1
                pos[1] += 1
            i += 1
        elif path[i] == 's':
            if path[i+1] == 'e':
                pos[0] += 1
                pos[1] -= 1
            elif path[i+1] == 'w':
                pos[1] -= 1
            i += 1
        i += 1

    key = tuple(pos)
    tiles[key] = 'black' if tiles[key] == 'white' or tiles[key] == () else 'white'

print("Part 1: ", sum(1 for x in tiles.values() if x == 'black'))

def toFlip(x, y, color):
    adjacent = [(x, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y), (x-1, y+1)]
    sumAdjacent = len([x for x in adjacent if tiles[x] == 'black'])
    if (sumAdjacent == 0 or sumAdjacent > 2) and color == 'black':
        return True
    elif sumAdjacent == 2 and color == 'white':
        return True
    return False

def createAdjacent(x, y):
    adjacent = [(x, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y), (x-1, y+1)]
    for a in adjacent:
        if tiles[a] == ():
            tiles[a] = 'white'

for _ in range(100):
    toChange = []
    for key, value in tiles.copy().items():
        createAdjacent(key[0], key[1])

    for key, value in tiles.copy().items():
        if toFlip(key[0], key[1], value):
            toChange.append(key)

    for tile in toChange:
        tiles[tile] = 'black' if tiles[tile] == 'white' or tiles[tile] == () else 'white'

print("Part 2: ", sum(1 for x in tiles.values() if x == 'black'))