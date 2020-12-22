from collections import defaultdict
f = open("input.txt", "r")

recipes, safe = [], []
ingredient_allergens = defaultdict(set)
recipe_index_allergens = defaultdict(list)
possible = {}

for i, line in enumerate(f.readlines()):
    ingredients, allergens = line.rstrip(')\n').split(' (contains ')

    ingredients = set(ingredients.split())
    allergens = set(allergens.split(', '))
    recipes.append(ingredients)

    for a in allergens:
        recipe_index_allergens[a].append(i)

    for ing in ingredients:
        ingredient_allergens[ing] |= allergens

for ing, allers in ingredient_allergens.items():
    safeTemp = set()

    for a in allers:
        for i in recipe_index_allergens[a]:
            if ing not in recipes[i]:
                safeTemp.add(a)
                break
    
    allers -= safeTemp
    if not allers:
        safe.append(ing)
    else:
        possible[ing] = allers

complete = {}
while len(possible) != len(complete):
    for ing, allers in possible.items():
        if len(allers) == 1 and allers:
            complete[ing] = allers

        for c in complete.values():
            if c.issubset(allers):
                possible[ing] = allers.difference(c)

complete = dict(sorted({aller.pop(): ing for ing, aller in complete.items()}.items()))

print("Part 1: ", sum(ingr in r for r in recipes for ingr in safe))
print("Part 2: ", ','.join(complete.values()))