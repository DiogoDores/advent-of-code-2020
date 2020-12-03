f = open("input.txt", "r")

grid = f.read().splitlines()

def countTrees(right, down):
    index, result = 0, 0
    for line in range(0, len(grid), down):
        if grid[line][index] == '#':
            result += 1
        index = (index + right) % len(grid[0])

    return result

print("Result 1: ", countTrees(3,1))
print("Result 2: ", countTrees(1,1) * countTrees(3,1) * countTrees(5,1) * countTrees(7,1) * countTrees(1,2))