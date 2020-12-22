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
            return cardsP1
        
        turns.add(turn)
        p1, p2 = cardsP1.pop(0), cardsP2.pop(0)

        if p1 <= len(cardsP1) and p2 <= len(cardsP2):
            winner = part_2(cardsP1[:p1], cardsP2[:p2])
        else:
            winner = cardsP1 if p1 > p2 else cardsP2
        
        if winner == cardsP1:
            cardsP1 += [p1, p2]
        else:
            cardsP2 += [p2, p1]

    print(winner)
    return winner

print('Part 1: ', part_1(cardsP1, cardsP2))

cardsP1, cardsP2 = [int(x) for x in cardsP1.split('\n')[1:]], [int(x) for x in cardsP2.split('\n')[1:]]
winner = part_2(cardsP1, cardsP2)
print('Part 2: ', sum([i*card for i, card in enumerate(winner[::-1], 1)]))