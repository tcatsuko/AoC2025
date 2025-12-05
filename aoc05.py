raw_input = []
f = open('aoc05.txt','rt')
for line in f:
    if line.strip() == '':
        raw_ranges = raw_input[:]
        raw_input = []
        continue
    raw_input += [line.strip()]
f.close()
ranges = []
for item in raw_ranges:
    split_range = [int(x) for x in item.split('-')]
    ranges += [split_range]
fresh_items = 0
for item in raw_input:
    ingredient = int(item)
    is_fresh = False
    for r_item in ranges:
        if ingredient in range(r_item[0], r_item[1] + 1):
            is_fresh = True
    if is_fresh == True:
        fresh_items += 1
print('Part 1: ' + str(fresh_items))

# Part 2.  Brute force want work.  So need to consolidate the overlapping ranges.

ranges.sort(key = lambda sublist:sublist[0])

made_changes = True
while made_changes == True:
    made_changes = False
    if len(ranges) == 1:
        break
    for index, item in enumerate(ranges):
        if index == len(ranges) - 1:
            break
        if made_changes == True:
            break
        current_index = index
        current_item = item
        next_index = index + 1
        next_item = ranges[next_index]
        if current_item[1] >= next_item[0] - 1:
            made_changes = True
            if current_item[1] > next_item[1]:
                del ranges[next_index]
            else:
                ranges[index] = [current_item[0], next_item[1]]
                del ranges[next_index]
possible_fresh = 0
for item in ranges:
    possible_fresh += item[1] - item[0] + 1
print('Part 2: ' + str(possible_fresh))
