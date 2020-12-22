from itertools import combinations
from collections import defaultdict
import math
f = open("input.txt", "r")

tiles = {}
directions = ['n', 'e', 's', 'w']

for section in f.read().split('\n\n'):
    key, grid = section.split('\n', 1)
    key = int(key.strip('Tile ').strip(':'))
    grid = grid.split('\n')
    tiles[key] = grid

def get_edge(grid, dir):
    if dir == 'n':
        return grid[0]
    elif dir == 'e':
        return ''.join([grid[row][-1] for row in range(len(grid))])
    elif dir == 's':
        return grid[-1]
    elif dir == 'w':
        return ''.join([grid[row][0] for row in range(len(grid))])
    else:
        print('Isso não é uma direção, estúpido')

def get_matching_sides():
    matchingSides = defaultdict(int)

    for key1, key2 in combinations(tiles, 2):
        grid1, grid2 = tiles[key1], tiles[key2]

        for side1 in directions:
            for side2 in directions:
                edge1, edge2 = get_edge(grid1, side1), get_edge(grid2, side2)

                if edge1 == edge2 or edge1 == edge2[::-1]:
                    matchingSides[key1] += 1
                    matchingSides[key2] += 1

    return matchingSides

matchingSides = get_matching_sides()
print("Part 1: ", math.prod(key for key, matches in matchingSides.items() if matches == 2))
