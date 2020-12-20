f = open("input.txt", "r")

ops = f.read().split('\n')
postfix, results = [], []

def part_1():
    for op in ops:
        infix = ' '.join(op).replace('   ', ' ').split()
        postfix, opstack = [], []

        while infix:
            x = infix.pop(0)

            if x in '+*(':
                if opstack and x in '+*' and opstack[-1] in '+*':
                    c = opstack.pop()
                    postfix.append(c)
                
                opstack.append(x)
            elif x == ')':
                for y in opstack[::-1]:
                    if y == '(':
                        opstack.pop()
                        break
                    else:
                        postfix.append(y)
                        opstack.pop()
            else:
                postfix.append(x)

        for y in opstack[::-1]:
            postfix.append(y)
        
        i = 0
        while len(postfix) != 1:
            if not postfix[i].isdigit():
                if postfix[i] == '*':
                    res = int(postfix[i-2]) * int(postfix[i-1])
                else:
                    res = int(postfix[i-2]) + int(postfix[i-1])
            
                postfix = postfix[:i-2] + [str(res)] + postfix[i+1:]
                i = 0
            i += 1

        results.append(int(postfix[0]))

def part_2():
    for op in ops:
        infix = ' '.join(op).replace('   ', ' ').split()
        postfix, opstack = [], []

        while infix:
            x = infix.pop(0)

            if x in '+*(':
                if opstack and x in '*+' and opstack[-1] in '+':
                    c = opstack.pop()
                    postfix.append(c)
                
                opstack.append(x)
            elif x == ')':
                for y in opstack[::-1]:
                    if y == '(':
                        opstack.pop()
                        break
                    else:
                        postfix.append(y)
                        opstack.pop()
            else:
                postfix.append(x)

        for y in opstack[::-1]:
            postfix.append(y)
        
        i = 0
        while len(postfix) != 1:
            if not postfix[i].isdigit():
                if postfix[i] == '*':
                    res = int(postfix[i-2]) * int(postfix[i-1])
                else:
                    res = int(postfix[i-2]) + int(postfix[i-1])
            
                postfix = postfix[:i-2] + [str(res)] + postfix[i+1:]
                i = 0
            i += 1

        results.append(int(postfix[0]))

part_1()
print('Part 1: ', sum(results))

results = []
part_2()
print('Part 2: ', sum(results))

