f = open("input.txt", "r")

inp = [int(line) for line in f.readlines()]
preamble, l = inp[:25], inp[25:]

def getEncryptionWeakness(preamble, code, n):
    target = getWeakness(preamble, code, n)

    currSum = inp[0]
    start = 0

    i = 1
    while i <= len(inp): 
        while currSum > target and start < i-1: 
            currSum -= inp[start]
            start += 1

        if currSum == target: 
            return min(inp[start:i-1]) + max(inp[start:i-1])

        if i < len(inp): 
            currSum += inp[i] 
        i += 1
    
def getWeakness(preamble, code, n):
    s = set()
    for i in range(0, len(preamble)):
        temp = n - preamble[i]
        if temp in s:
            newPreamble, newList = preamble[1:] + [n], code[1:]
            return getWeakness(newPreamble, newList, code[code.index(n) + 1])
        s.add(preamble[i])

    return n

print("Part 1: ", getWeakness(preamble, l, l[0]))
print("Part 2: ", getEncryptionWeakness(preamble, l, l[0]))