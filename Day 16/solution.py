import copy
f = open("input.txt", "r")

myTicket, tickets, invalid = [], [], []
restrictions = {}

for line in f:
    if line == '\n':
        continue

    if 'your' in line:
        myTicket = list(map(int, next(f).strip().split(',')))
    elif 'nearby' in line:
        for line in f.readlines():
            tickets.append(list(map(int, line.strip().split(','))))
    else:
        field, rules = line.split(': ')
        rules = rules.split(' or ')
        rules = [rule.split('-') for rule in rules]
        restrictions[field] = [[int(num) for num in rule] for rule in rules]

for ticket in tickets:
    for number in ticket:
        valid = False
        for r in restrictions:
            min1, min2 = restrictions[r][0][0], restrictions[r][1][0]
            max1, max2 = restrictions[r][0][1], restrictions[r][1][1]

            if number in range(min1, max1 + 1) or number in range(min2, max2 + 1):
                valid = True
                break
        
        if not valid:
            invalid.append(number)

print("Part 1: ", sum(invalid))

valid_tickets = []
for ticket in tickets:
    is_valid = True
    for num in ticket:
        if num in invalid:
            is_valid = False
            break
    if is_valid:
        valid_tickets.append(ticket)

fields = []
for i in range(len(tickets[0])):
    fields.append([ticket[i] for ticket in valid_tickets])

r_res = copy.deepcopy(restrictions)
correct_field = {}
for f in fields:
    for r in r_res:
        min1, min2 = r_res[r][0][0], r_res[r][1][0]
        max1, max2 = r_res[r][0][1], r_res[r][1][1]

        if all((min1 <= n <= max1 or min2 <= n <= max2) for n in f):
            correct_field.setdefault(r, []).append(fields.index(f))

c_f = dict()
for f1 in correct_field:
    for f2 in correct_field:
        chk = set(correct_field[f1]).difference(set(correct_field[f2]))
        if len(chk) == 1:
            c_f[f1] = chk.pop()

total = 1
for f in c_f:
    if 'departure' in f:
        total *= myTicket[c_f[f]]

print("Part 2: ", total)