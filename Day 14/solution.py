f = open("input.txt", "r")

def part_1():
    mask = 0
    mem = {}
    for line in f.read().split('\n'):
        if 'mask' in line:
            mask = line[line.find('=') + 2:]
        else:
            pos = int(line[line.find('[') + 1 : line.find(']')])
            binary = bin(int(line[line.find('=') + 2:]))[2:]
            binary_str = str(binary).zfill(len(mask))

            for i in range(len(binary_str)):
                if mask[i] != 'X':
                    binary_str = binary_str[:i] + mask[i] + binary_str[i + 1:]
            
            mem[pos] = int(str(int(binary_str)), 2)

    return sum(x for x in mem.values())

def part_2(instructions):
    mask, memory = '', {}
    for instruction, value in instructions:
        if instruction == 'mask':
            mask = value
        else:
            address = bin(int(instruction))[2:].zfill(36)
            address = [bit_mask if bit_mask in '1X' else bit_address for bit_address, bit_mask in zip(address, mask)]
            xs = [i for i, bit in enumerate(address) if bit == 'X']
            for combination in range(1 << len(xs)):
                for i, bit in enumerate(bin(combination)[2:].zfill(len(xs))):
                    address[xs[i]] = bit
                memory[''.join(address)] = int(value)
    return sum(memory.values())

print("Part 1: ", part_1())
f.close()
f = open("input.txt", "r")

instructions = [line.replace('mem', '').replace('[', '').replace(']', '').split(' = ') for line in f.read().splitlines()]

print("Part 2: ", part_2(instructions))