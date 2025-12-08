import networkx as nx
from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', ['x', 'y','z'])
raw_input = []
f = open('aoc08.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()
def distance(pair):
    p1, p2 = pair
    distance = sqrt((p2.x - p1.x)**2 + (p2.y-p1.y)**2 + (p2.z-p1.z)**2)
    return distance
point_pairs = []
points = []
for line in raw_input:
    x,y,z = [int(x) for x in line.split(',')]
    points += [Point(x,y,z)]
for i, p1 in enumerate(points):
    for p2 in points[i+1:]:
        point_pairs += [(p1, p2)]
point_pairs.sort(key=lambda pair:distance(pair))

# Take the top 10 pairs
G = nx.Graph()
for pair in point_pairs[:1000]:
    G.add_edge(pair[0], pair[1])
circuits = list(nx.connected_components(G))
circuits.sort(key=lambda x:len(x))
circuit_lengths = []
for item in circuits[::-1]:
    circuit_lengths += [len(item)]
part1 = circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]
print('Part 1: ' + str(part1))
final_pair = None
for pair in point_pairs[1000:]:
    G.add_edge(pair[0], pair[1])
    if nx.is_connected(G) == True and all(G.has_node(node) for node in points) == True:
        final_pair = pair
        break
if final_pair != None:
    part2 = final_pair[0].x * final_pair[1].x
print('Part 2: ' + str(part2))