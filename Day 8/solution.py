import copy
f = open("input.txt", "r")

code = [line.split(' ') for line in f.read().split('\n')]
finished, result = False, 0

def get_indexes():
    return {index:val for index, val in enumerate(code) if val[0] in ['jmp', 'nop']}

def run_code(acc, codeCpy):
    visited, i = [], 0
    
    while True:

        if i in visited:
            return False, acc

        visited.append(i)
        if codeCpy[i][0] == 'acc':
            acc += int(codeCpy[i][1])

        if i == len(codeCpy) - 1:
            return True, acc

        if codeCpy[i][0] == 'jmp':
            i += int(codeCpy[i][1]) - 1

        i += 1

def brute_force(indexes):
    for k,_ in indexes.items():
        codeCopy = copy.deepcopy(code)

        if codeCopy[k][0] == 'nop':
            codeCopy[k][0] = 'jmp'
        else:
            codeCopy[k][0] = 'nop'

        finished, acc = run_code(0, codeCopy)

        if finished:
            return acc


print("Part 1: ", run_code(0, code)[1])
print("Part 2: ", brute_force(get_indexes()))