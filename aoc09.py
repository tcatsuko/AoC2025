from collections import namedtuple
from shapely import Polygon


raw_input = []
f = open('aoc09.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()

Point = namedtuple('Point',['x','y'])

points = []

largest_rect = 0
for line in raw_input:
    x, y = [int(x) for x in line.split(',')]
    points += [Point(x,y)]
for i, p1 in enumerate(points):
    for p2 in points[i:]:
        area = (abs(p2.x-p1.x) + 1) * (abs(p2.y-p1.y) + 1)
        if area > largest_rect:
            largest_rect = area
print('Part 1: ' + str(largest_rect))

# Use shapely to create a polygon containing the points
s_points = points[:]
s_points += [points[0]]
polygon = Polygon(s_points)
largest_rect = 0
for i, p1 in enumerate(points):
    for p2 in points[i:]:
        area = (abs(p2.x-p1.x) + 1) * (abs(p2.y-p1.y) + 1)
        if area > largest_rect:
            # Determine rectangle coords
            UL = (min(p1.x, p2.x), min(p1.y,p2.y))
            UR = (max(p1.x, p2.x), min(p1.y, p2.y))
            LR = (max(p1.x, p2.x), max(p1.y, p2.y))
            LL = (min(p1.x, p2.x), max(p1.y, p2.y))
            rect_coords = [UL, UR, LR, LL, UL]
            poly_rect = Polygon(rect_coords)
            if polygon.contains(poly_rect):
                largest_rect = area
print('Part 2: ' + str(largest_rect))
    
