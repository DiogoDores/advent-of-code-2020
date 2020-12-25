def play_game(cups, rounds):
    circle = dict(zip(cups, cups[1:] + cups[:1]))
    current_label = cups[-1]
    for _ in range(rounds):
        current_label = circle[current_label]

        pick_up = list()
        tmp_label = current_label
        for _ in range(3):
            tmp_label = circle[tmp_label]
            pick_up.append(tmp_label)
        circle[current_label] = circle[tmp_label]

        destination_label = current_label - 1
        while destination_label in pick_up or destination_label < 1:
            destination_label -= 1
            if destination_label < 1:
                destination_label = max(cups)

        circle[destination_label], circle[pick_up[-1]] = pick_up[0], circle[destination_label]

    return circle

cups_p1 = list(map(int, '974618352'))
circle = play_game(cups_p1, 100)
next_ = 1
for _ in range(8):
    next_ = circle[next_]
    print(next_, end='')

print('\n\n')
cups_p2 = cups_p1 + list(range(10, int(1e6) + 1))
circle = play_game(cups_p2, int(1e7))
ans = 1
next_ = 1
for _ in range(2):
    next_ = circle[next_]
    ans *= next_
print(ans)