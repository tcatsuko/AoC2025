raw_input = []
f = open('aoc06.txt','rt')
for line in f:
    raw_input += [line.strip().split(' ')]
f.close()
cleaned_numbers = []
for line in raw_input:
    current_line = []
    for item in line:
        if item != '':
            current_line += [item]
    cleaned_numbers += [current_line]
cleaned_numbers = [list(x) for x in zip(*cleaned_numbers)]
total = 0
for line in cleaned_numbers:
    operator = line[-1]
    numbers = [int(x) for x in line[:-1]]
    current_operation = numbers[0]
    for number in numbers[1:]:
        if operator == '+':
            current_operation += number
        elif operator == '*':
            current_operation *= number
        else:
            print('UNKNOWN OPERATOR')
    total += current_operation
print('Part 1: ' + str(total))

raw_input = []
f = open('aoc06.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()

# Figure out how many columns there are
operators = raw_input[-1]
column_info = []
# Need to determine column widths.  THEY ARE NOT UNIFORM
start_col = 0
for x in range(1,len(operators)):
    if operators[x] != ' ':
        col_length = x - start_col
        column_info += [(start_col, col_length)]
        start_col = x
column_info += [(start_col, len(operators) - start_col + 1)]
num_columns = len(operators)
intermediate_numbers = []
total = 0
for info in column_info:
    num_line = []
    for line in raw_input:
        num_line += [line[info[0] : info[0] + info[1]]]
    intermediate_numbers += [num_line]
numbers = intermediate_numbers
for line in numbers:
    reversed = [x[::-1] for x in line]
    op = reversed[-1]
    op = op.replace(' ','')
    intermed = reversed[:-1]
    operands = []
    for x in range(len(intermed[0])):
        temp_num = ''
        for y in intermed:
            temp_num += y[x]
        temp_num = temp_num.replace(' ','')
        if temp_num != '':
            operands += [int(temp_num)]
    current_operation = operands[0]
    for item in operands[1:]:
        if op == '*':
            current_operation *= item
        elif op == '+':
            current_operation += item
        else:
            print('INVALID OP')
    total += current_operation
print('Part 2: ' + str(total))