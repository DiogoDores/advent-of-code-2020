f = open("input.txt", "r")

seats = [list(line.strip()) for line in f.read().split('\n')]

def count_occupied(grid, i, j, h, w):
    conditions = [
        i > 0 and j > 0 and grid[i - 1][j - 1] == '#',
        i > 0 and grid[i - 1][j] == '#',
        i > 0 and j < w - 1 and grid[i - 1][j + 1] == '#', 
        j > 0 and grid[i][j - 1] == '#',
        j < w - 1 and grid[i][j + 1] == '#',
        i < h - 1 and j > 0 and grid[i + 1][j - 1] == '#',
        i < h - 1 and grid[i + 1][j] == '#',
        i < h - 1 and j < w - 1 and grid[i + 1][j + 1] == '#',
    ]

    return sum(int(c) for c in conditions)

def fill_seats(seats):
    newGrid = []
    changed = False
    for i, row in enumerate(seats):
        newRow = []
        for j, _ in enumerate(row):
            if seats[i][j] == 'L' and count_occupied(seats, i, j, len(seats), len(row)) == 0:
                newRow.append('#')
                changed = True
            elif seats[i][j] == '#' and count_occupied(seats, i, j, len(seats), len(row)) >= 4:
                newRow.append('L')
                changed = True
            else:
                newRow.append(seats[i][j])
        newGrid.append(newRow)
    return newGrid, changed

while True:
    seats, changed = fill_seats(seats)
    if not changed:
        break

print("Part 1:", sum(row.count("#") for row in seats))

# Part 2

grid = [list(line.strip()) for line in open('input.txt')]
height = len(grid)
width = len(grid[0])
neighbors = [[list() for _ in range(width)] for _ in range(height)]

# east-west
for i, row in enumerate(grid):
    seats = [j for j, node in enumerate(row) if node != "."]
    for j1, j2 in zip(seats[:-1], seats[1:]):
        neighbors[i][j1].append((i, j2))
        neighbors[i][j2].append((i, j1))

# north-south
for j in range(width):
    seats = [i for i in range(height) if grid[i][j] != "."]
    for i1, i2 in zip(seats[:-1], seats[1:]):
        neighbors[i1][j].append((i2, j))
        neighbors[i2][j].append((i1, j))
               
all_coords = [(i, j) for j in range(width) for i in range(height) if grid[i][j] != '.']

# diagonal \
d = height - 1
while True:
    this_coord = [(u, v) for u, v in all_coords if u - v == d]

    if len(this_coord) == 0:
        break
    for ((i1, j1), (i2, j2)) in zip(this_coord[:-1], this_coord[1:]):
        neighbors[i1][j1].append((i2, j2))
        neighbors[i2][j2].append((i1, j1))
    d -= 1

# diagonal /
d = 0
while True:
    this_coord = [(u, v) for u, v in all_coords if u + v == d]
    
    if len(this_coord) == 0:
        break
    for ((i1, j1), (i2, j2)) in zip(this_coord[:-1], this_coord[1:]):
        neighbors[i1][j1].append((i2, j2))
        neighbors[i2][j2].append((i1, j1))
    d += 1


this_grid = [[v for v in row] for row in grid]

changed = True
while changed:
    new_grid = []
    changed = False
    for i, row in enumerate(this_grid):
        new_row = []
        for j, seat in enumerate(row):
            cur_val = this_grid[i][j]
            if cur_val == ".":
                new_row.append(".")
            else:    
                occupied = sum(int(this_grid[u][v] == '#') for u, v in neighbors[i][j])
                if occupied == 0 and cur_val == "L":
                    new_row.append("#")
                    changed = True
                elif occupied >= 5 and cur_val == "#":
                    new_row.append("L")
                    changed = True
                else:
                    new_row.append(cur_val)
        new_grid.append(new_row)
    this_grid = new_grid


print("Part 2:", [v for row in this_grid for v in row].count("#"))