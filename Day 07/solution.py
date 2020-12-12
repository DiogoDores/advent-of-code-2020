f = open("input.txt", "r")

bags = []

#PART 1 - TODO ONE DAY :)
def find_bags(bags_to_search, sumBags):
    for b in bags_to_search:
        for bag in bags:
            if any(b in smallBags for smallBags in bag[1:]) and bag[0] not in bags_to_search:
                bags_to_search.append(bag[0])
                sumBags += 1

    return sumBags

#PART 2
def count_bags(currBag):
    
    cnt = 0
    children = []

    for bag in bags:
        if currBag == bag[0]:
            children = [item for item in bag[1:]]
    
    for child in children:
        if child:
            cnt += int(child[0]) + int(child[0]) * count_bags(child[1])

    return cnt
    

#PARSING
for line in f.readlines():
    raw = line.replace('bags', '').replace('bag', '').replace(' contain ', ', ').replace('other', '').replace('.', '').replace(' \n', '').split(' , ')

    for i in range(1, len(raw)):
        if 'no' in raw[i]:
            raw[i] = []
        else:
            raw[i] = [raw[i][0], raw[i][2:]]

    bags.append(raw)

bags_to_search, sumBags = ['shiny gold'], 0

#RESULTS
print("Part 1: ", find_bags(bags_to_search, sumBags))
print("Part 2: ", count_bags('shiny gold'))
