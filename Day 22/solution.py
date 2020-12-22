from collections import deque
f = open("input.txt", "r")

cardsP1, cardsP2 = f.read().split('\n\n')

def part_1(cardsP1, cardsP2): 
    cardsP1, cardsP2 = [int(x) for x in cardsP1.split('\n')[1:]], [int(x) for x in cardsP2.split('\n')[1:]]
    while cardsP1 and cardsP2:
        p1, p2 = cardsP1.pop(0), cardsP2.pop(0)
        
        if p1 > p2:
            cardsP1 += [p1, p2]
        else:
            cardsP2 += [p2, p1]

    winner = cardsP1 if cardsP1 else cardsP2
    return sum([i*card for i, card in enumerate(winner[::-1], 1)])

def part_2(cardsP1, cardsP2):
    turns = set()
    winner = []
    while cardsP1 and cardsP2:
        turn = (tuple(cardsP1), tuple(cardsP2))
        if turn in turns:
            return cardsP1, cardsP1
        
        turns.add(turn)
        p1, p2 = cardsP1.popleft(), cardsP2.popleft()

        if p1 <= len(list(cardsP1)) and p2 <= len(list(cardsP2)):
            p1Wins, _ = part_2(deque(list(cardsP1)[:p1]), deque(list(cardsP2)[:p2]))
        else:
            p1Wins = p1 > p2
        
        if p1Wins:
            cardsP1.extend([p1, p2])
        else:
            cardsP2.extend([p2, p1])

    return cardsP1, cardsP1 or cardsP2

print('Part 1: ', part_1(cardsP1, cardsP2))

cardsP1, cardsP2 = deque([int(x) for x in cardsP1.split('\n')[1:]]), deque([int(x) for x in cardsP2.split('\n')[1:]])
winner = part_2(cardsP1, cardsP2)[1]
print('Part 2: ', sum([i*card for i, card in enumerate(list(winner)[::-1], 1)]))