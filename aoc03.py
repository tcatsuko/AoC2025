raw_input = []
f = open('aoc03.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()
battery_banks = []
for line in raw_input:
    battery_banks += [[int(x) for x in line]]

def joltage(bank, remaining_cells):
    length = len(bank)
    if remaining_cells > 1:
        max_battery = max(bank[:length - (remaining_cells - 1)])
        max_index = bank.index(max_battery)
    else:
        max_battery = max(bank)
        max_index = bank.index(max_battery)
    if remaining_cells == 1:
        return max_battery    
    next_max = joltage(bank[max_index + 1:], remaining_cells - 1)
    max_string = str(max_battery)
    next_max_string = str(next_max)
    return int(max_string + next_max_string)

output_joltage = 0
batteries = 2
for bank in battery_banks:

    bank_joltage = joltage(bank, batteries)
    output_joltage += bank_joltage
print('Part 1: ' + str(output_joltage))

output_joltage = 0
batteries = 12
for bank in battery_banks:

    bank_joltage = joltage(bank, batteries)
    output_joltage += bank_joltage
print('Part 2: ' + str(output_joltage))