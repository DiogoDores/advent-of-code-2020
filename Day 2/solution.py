f = open("input.txt", "r")

result1, result2 = 0, 0
for line in f.readlines():
    hyphen, space, colon = line.find('-'), line.find(' '), line.find(':')
    mini, maxi = int(line[0:hyphen]), int(line[hyphen + 1: space])
    symbol, passw = line[space + 1:colon], line[colon+2:]

    #Part 1
    if passw.count(symbol) >= mini and passw.count(symbol) <= maxi:
        result1 += 1
    #Part 2
    if (passw[mini-1] == symbol and passw[maxi-1] != symbol) or (passw[mini-1] != symbol and passw[maxi-1] == symbol):
        result2 += 1

print("Result Part 1: ", result1)
print("Result Part 2: ", result2)