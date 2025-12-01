raw_input = []

f = open('aoc01.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()
dial = 50 
zero_counter = 0
for line in raw_input:
    direction = line[0]
    magnitude = int(line[1:])
    if direction == 'L':
        dial = (dial - magnitude) % 100
    else:
        dial = (dial + magnitude) % 100
    if dial == 0:
        zero_counter += 1
print('Part 1: The dial pointed at zero ' + str(zero_counter) + ' times.')

dial = 50 
zero_counter = 0
for line in raw_input:
    direction = line[0]
    magnitude = int(line[1:])
    multiplier = magnitude // 100
    magnitude -= (100 * multiplier)
    if direction == 'L':
        newdial = dial - magnitude
        if newdial < 0 and dial != 0:
            zero_counter += 1
        dial = newdial % 100
    else:
        newdial = dial + magnitude
        if newdial > 100 and dial != 0:
            zero_counter += 1
        dial = newdial % 100
    zero_counter += multiplier
    if dial == 0:
        zero_counter += 1
print('Part 2: The dial sees zero ' + str(zero_counter) + ' times.')