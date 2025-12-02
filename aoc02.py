raw_input = []
f = open('aoc02.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()
ranges = line.split(',')
invalid = 0
invalid_sum = 0
for item in ranges:
    start, end = item.split('-')
    for x in range(int(start), int(end) + 1):
        str_x = str(x)
        if len(str_x) % 2 == 0:
            first_half = str_x[:len(str_x) // 2]
            repeat_count = str_x.count(first_half)
            if repeat_count == 2:
                invalid += 1
                invalid_sum += x
print('Part 1: invalid ID sum is  ' + str(invalid_sum) )

invalid_sum = 0

for item in ranges:
    start, end = item.split('-')
    for x in range(int(start), int(end) + 1):
        invalid_set = set()
        str_x = str(x)
        id_length = len(str_x)
        biggest_length = id_length // 2
        for y in range(1, biggest_length + 1):
            if id_length % y != 0:
                continue
            substring = str_x[:y]
            sub_count = str_x.count(substring)
            repeats = id_length // y
            if sub_count == repeats:
                if x not in invalid_set:
                    invalid_sum += x
                    invalid_set.add(x)
print('Part 2: invalid ID sum is  ' + str(invalid_sum))              
