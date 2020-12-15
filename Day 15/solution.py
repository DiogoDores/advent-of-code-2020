numbers = [6,13,1,15,2,0]
memory = {n: i + 1 for i, n in enumerate(numbers[:-1])}

def find_number(cap):
    for i in range(len(numbers), cap):
        numbers.append(i - memory.get(numbers[-1], i))
        memory[numbers[-2]] = i

    return numbers[-1]

print("Part 1: ", find_number(2020))
print("Part 2: ", find_number(30000000))