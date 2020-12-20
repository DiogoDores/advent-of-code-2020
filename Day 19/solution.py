import re
f = open("input.txt", "r")

rules_txt, messages_txt = f.read().split('\n\n')
rules = {}

for line in rules_txt.splitlines():
    key, steps = line.split(': ')
    rules[key] = steps.replace('"', '')

messages = messages_txt.split('\n')


def follow_rules(key):
    if rules[key] in 'ab':
        return rules[key]

    steps = rules[key].split(" | ")
    for i, step in enumerate(steps):
        steps[i] = '(' + ''.join(follow_rules(s) for s in step.split()) + ')'

    return '(' + '|'.join(steps) + ')'

valid = follow_rules('0')
print('Part 1: ', sum(1 for msg in messages if re.match(f"^{valid}$", msg)))

cnt1, cnt2 = 0, 1
index = 2

while cnt1 != cnt2:
    rules['8'] = '42' + (' |' if index > 2 else '') + ' |'.join(' 42' * i for i in range(2, index))
    rules['11'] = '42 31' + (' |' if index > 2 else '') + ' |'.join(' 42' * i + ' 31' * i for i in range(2, index))
    valid = follow_rules('0')
    counter = 0
    for msg in messages:
        if re.match(f"^{valid}$", msg):
            counter += 1

    cnt2 = cnt1
    cnt1 = counter
    index += 1

print("Part 2: ", cnt1)


