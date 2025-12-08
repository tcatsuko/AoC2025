from functools import cache
raw_input = []
f = open('aoc07.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()
beams = set()
initial_x_pos = -1
# Find the start
for col, item in enumerate(raw_input[0]):
    if item == 'S':
        beams.add((col, 0))
        initial_x_pos = col
splits = 0
for y, row in enumerate(raw_input):
    for x, item in enumerate(row):
        if item == '^':
            # check above
            if (x, y-1) in beams:
                # Good split
                splits += 1
                beams.add((x-1,y))
                beams.add((x+1, y))
        else:
            if (x, y-1) in beams:
                beams.add((x, y))
print('Part 1: ' + str(splits))
            
@cache
def quantum(x, y):
    if y == len(raw_input): # Exit manifold
        return 1
    if raw_input[y][x] == '^': # Split the beam
        return quantum(x-1,y) + quantum(x+1,y)
    else:
        return quantum(x, y+1) # Propogate the beam in the current cell

timelines = quantum(initial_x_pos, 0)
print('Part 2: ' + str(timelines))
