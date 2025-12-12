raw_input = []
f = open('aoc12.txt.','rt')
for line in f:
    raw_input += [line.strip()]
f.close()

# Parse it
presents = []
regions = []

current_present = []
# Get all of the present configs first
for raw_index, line in enumerate(raw_input[1:]):
    if line == '':
        continue
    if 'x' in line:
        presents += [current_present]
        region_start = raw_index + 1
        break
    if ':' in line:
        presents += [current_present]
        current_present = []
        continue
    
    current_present += [line]

# get all of the regions
for line in raw_input[region_start:]:
    size, config = line.split(': ')
    x,y = [int(x) for x in size.split('x')]
    present_count = [int(x) for x in config.split(' ')]
    regions +=[ [[x,y],present_count]]
def get_present_area(present):
    area = 0
    for line in present:
        area += line.count('#')
    return area

valid_regions = 0
valid_region_info = []
# Sanity check to see if there is even enough area
for region in regions:
    size, config = region
    region_area = size[0] * size[1]
    total_present_area = 0
    for present, quantity in enumerate(config):
        present_area = get_present_area(presents[present])
        total_present_area += (present_area * quantity )
    if total_present_area <= region_area:
        valid_regions += 1
        valid_region_info += [region]

# out of curiosity, it can't be this easy.  Check answer based 
# solely on area.        
print('Part 1: ' + str(valid_regions))
# IT WORKED
