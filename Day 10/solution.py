f = open("example.txt", "r")

joltages = sorted([int(i) for i in f.readlines()])

def count_ways():
    ways = {0 : 1}

    for jolt in joltages:
        cnt = 0
        for i in range(1, 4):
            if jolt - i in ways:
                cnt += ways[jolt - i]
        ways[jolt] = cnt

    return ways[joltages[len(joltages) - 1]]


def count_diffs():
    currJolt, diffs = 0, []
    for jolt in joltages:
        if jolt in range(currJolt + 4):
            diffs.append(jolt - currJolt)
            currJolt = jolt

    return diffs.count(1) * (diffs.count(3) + 1)

print("Part 1: ", count_diffs())
print("Part 2: ", count_ways())