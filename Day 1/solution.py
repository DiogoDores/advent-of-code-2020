f = open("input.txt", "r")
numbers = [int(i) for i in f.readlines()]


#PART 1
result1 = 0

for i in numbers:
    j = i + 1
    for j in numbers:
        if (i+j == 2020):
            result1 = i*j
            break
print(result1)

#PART 2

result2 = 0

for i in numbers:
    j = i + 1
    for j in numbers:
        k = i + 2
        for k in numbers:
            if (i+j+k == 2020):
                result2 = i*j*k
                break
print(result2)