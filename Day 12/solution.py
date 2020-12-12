import math, copy
f = open("input.txt", "r")

instructions = [[line[0], int(line[1:])] for line in f.read().split('\n')]
directions = ['N', 'E', 'S', 'W']

def change_boat_direction(instruct, amount, direction):

    index = directions.index(direction)
    if amount == 90:
        amount = 1
    elif amount == 180:
        amount = 2
    else:
        amount = 3

    if instruct == 'L':
        index -= amount
    else:
        index += amount

    return directions[index % 4]

def change_waypoint_direction(instruct, angle, x, y):

    if instruct == 'R':
        angle = -angle
    
    angle_rad = math.radians(angle)

    x1 = int(x * math.cos(angle_rad)) - int(y * math.sin(angle_rad))
    y1 = int(x * math.sin(angle_rad)) + int(y * math.cos(angle_rad))

    return x1, y1


def move(inst, x, y):
    if inst[0] == 'N':
        y += inst[1]
    elif inst[0] == 'S':
        y -= inst[1]
    elif inst[0] == 'E':
        x += inst[1]
    elif inst[0] == 'W':
        x -= inst[1]

    return x, y

def get_boat_position(direction):
    instructions_cpy = copy.deepcopy(instructions)
    x, y = 0, 0

    for inst in instructions_cpy:
        if inst[0] == 'F':
            inst[0] = direction

        if inst[0] in 'LR':
            direction = change_boat_direction(inst[0], inst[1], direction)
        else:
            x, y = move(inst, x, y)

    return abs(x) + abs(y)

def get_waypoint_position(x, y):
    waypointX, waypointY = x, y
    shipX, shipY = 0, 0

    for inst in instructions:

        if inst[0] == 'F':
            shipX += inst[1] * waypointX
            shipY += inst[1] * waypointY
        elif inst[0] in 'LR':
            waypointX, waypointY = change_waypoint_direction(inst[0], inst[1], waypointX, waypointY)
        else:
            waypointX, waypointY = move(inst, waypointX, waypointY)

    return abs(shipX) + abs(shipY)

print("Part 1: ", get_boat_position('E'))
print("Part 2: ", get_waypoint_position(10, 1))