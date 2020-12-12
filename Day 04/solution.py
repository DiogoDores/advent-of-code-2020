import re
f = open("input.txt", "r")

result1, result2 = 0, 0
codes = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validateData(line):
    byr = line.split(codes[0])[1].split()[0]
    iyr = line.split(codes[1])[1].split()[0]
    eyr = line.split(codes[2])[1].split()[0]
    hgt = line.split(codes[3])[1].split()[0]
    hcl = line.split(codes[4])[1].split()[0]
    ecl = line.split(codes[5])[1].split()[0]
    pid = line.split(codes[6])[1].split()[0]

    if not byr.isdigit() or int(byr) < 1920 or int(byr) > 2002:
        return False
    if not iyr.isdigit() or int(iyr) < 2010 or int(iyr) > 2020:
        return False
    if not eyr.isdigit() or int(eyr) < 2020 or int(eyr) > 2030:
        return False

    if 'cm' in hgt:
        if not hgt.split('cm')[0].isdigit() or int(hgt.split('cm')[0]) < 150 or int(hgt.split('cm')[0]) > 193:
            return False
    elif 'in' in hgt:
        if not hgt.split('in')[0].isdigit() or int(hgt.split('in')[0]) < 59 or int(hgt.split('in')[0]) > 76:
            return False
    elif ('cm' or 'in') not in hgt:
        return False

    if re.match('^#[0-9a-f]{6}$', hcl) == None:
        return False
    if ecl not in eye_color:
        return False
    if not pid.isdigit() or len(pid) != 9:
        return False

    return True

for line in f.read().split("\n\n"):
    if all(code in line for code in codes):
        result1 += 1
        result2 += validateData(line)

print("Result 1: ", result1)
print("Result 2: ", result2)