from functools import cache

raw_input = []
f = open('aoc11.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()

nodes = {}
for line in raw_input:
    parent, children = line.split(': ')
    children = children.split(' ')
    nodes[parent] = children

@cache
def traverse(in_node, exit_node, part2 = False, dac = False, fft = False):
    if part2 == True:
        if in_node == exit_node and dac == True and fft == True:
            return 1
        elif in_node == exit_node and (dac == False or fft == False):
            return 0 # Did not go through either of the two required nodes
    else:
        if in_node == exit_node:
            return 1
    if in_node == 'dac':
        dac = True
    if in_node == 'fft':
        fft = True
    return sum([traverse(x, exit_node, part2, dac, fft) for x in nodes[in_node]])

num_paths = traverse('you','out')
print('Part 1: ' + str(num_paths))

raw_input = []
f = open('aoc11.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()

nodes = {}
for line in raw_input:
    parent, children = line.split(': ')
    children = children.split(' ')
    nodes[parent] = children

num_paths = traverse('svr', 'out', part2 = True, dac = False, fft = False)
print('Part 2: ' + str(num_paths))