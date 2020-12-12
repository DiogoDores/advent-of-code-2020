f = open("input.txt", "r")

result1, result2 = 0, 0

for line in f.read().split("\n\n"):
    result1 += len(set(''.join(line.split('\n'))))

    questions = []
    for i in line.split('\n'):
        questions.append(set(char for char in i))
    
    result2 += len(questions[0].intersection(*questions))
    

print("Part 1: ", result1)
print("Part 2: ", result2)