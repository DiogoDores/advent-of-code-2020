import math, sys
from functools import reduce
f = open("input.txt", "r")

target = int(f.readline())
line1 = f.readline()
line2 = line1
buses = [int(x) for x in line1.replace('x,', '').replace('x', ' ').split(',')]
idts = [(i, int(t)) for i, t in enumerate(line2.split(",")) if t != "x"]

print(idts)

bestTime = 0
targetDelta, newDelta = sys.maxsize, sys.maxsize
for bus in buses:
    lower = bus * math.floor(target/bus)
    upper = bus * math.ceil(target/bus)
    
    if lower > target:
        newDelta = lower - target
    elif upper > target:
        newDelta = upper - target

    if targetDelta > newDelta:
        targetDelta = newDelta
        bestTime = bus

print("Part 1: ", bestTime * targetDelta)

best, bestid, prod, start = 10 ** 10, 0, 1, 0
for _, t in idts:
    prod *= t
    if (wait := start + t - start % t) < best:
        best, bestid = wait, t

res = 0
for i, t in idts:
    p = prod // t
    res += -i * pow(p, -1, t) * p

print("Part 2: ", res % prod)