raw_input = []
f = open('aoc04.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()

rows = len(raw_input)
cols = len(raw_input[0])

# Time to do some padding
floor_map = []
floor_map += [[x for x in '.' * (cols + 2)]]
for line in raw_input:
    floor_map += [[x for x in '.' + line + '.']]
floor_map += [[x for x in '.' * (cols + 2)]]

def check_roll(pos, floor_map):
    x, y = pos
    rolls_in_range = 0
    if floor_map[y-1][x-1] == '@':
        rolls_in_range += 1
    if floor_map[y-1][x] == '@':
        rolls_in_range += 1
    if floor_map[y-1][x+1] == '@':
        rolls_in_range += 1
    if floor_map[y][x-1] == '@':
        rolls_in_range += 1
    if floor_map[y][x+1] == '@': 
        rolls_in_range += 1
    if floor_map[y+1][x-1] == '@':
        rolls_in_range += 1
    if floor_map[y+1][x] == '@':
        rolls_in_range += 1
    if floor_map[y+1][x+1] == '@':
        rolls_in_range += 1
    return rolls_in_range

reachable = 0
for y, row in enumerate(floor_map):
    for x, item in enumerate(row):
        if item == '@':
            rolls_in_range = check_roll((x, y), floor_map)
            if rolls_in_range < 4:
                reachable += 1

print('Part 1: ' + str(reachable))

# Now for part 2
reachable = 0
removed_roll = True
while removed_roll == True:
    removed_roll = False
    removed_rolls = []
    for y, row in enumerate(floor_map):
        for x, item in enumerate(row):
            if item == '@':
                rolls_in_range = check_roll((x, y), floor_map)
                if rolls_in_range < 4:
                    reachable += 1
                    removed_rolls += [(x, y)]
                    removed_roll = True
    for roll in removed_rolls:
        x, y = roll
        floor_map[y][x] = '.'
print('Part 2: ' + str(reachable))