import z3

raw_input = []
f = open('aoc10.txt','rt')
for line in f:
    raw_input += [line.strip()]
f.close()
lights = []
buttons = []
buttons_raw = []
joltages = []

# Parse the input
for line in raw_input:
    split_line = line.split(' ')
    # Determine how many lights there are
    num_lights = len(split_line[-1].split(','))
    current_lights = ['0'] * num_lights
    # First set the desired light config
    desired_lights = split_line[0]
    for i, item in enumerate(desired_lights[1:-1]):
        if item == '#':
            current_lights[i] = '1'
    current_lights = ''.join(current_lights)
    lights += [int(current_lights, 2)]
    
    # Next set the button wirings
    wirings = split_line[1:-1]
    current_set_wiring = []
    current_set_wiring_raw = []
    for button_config in wirings:
        final_wiring = 0
        for ind_button in button_config[1:-1].split(','):
            current_wiring = ['0'] * num_lights
            current_wiring[int(ind_button)] = '1'
            current_wiring = ''.join(current_wiring)
            final_wiring += int(current_wiring, 2)
        current_set_wiring += [final_wiring]
        current_set_wiring_raw += [[int(x) for x in button_config[1:-1].split(',')]]
    buttons += [current_set_wiring]
    current_set_wiring_raw = [tuple(x) for x in current_set_wiring_raw]
    buttons_raw += [current_set_wiring_raw]
    
    # Now get joltages.  Don't need it for part 1 but I suspect we will for part 2
    current_joltages = [int(x) for x in split_line[-1][1:-1].split(',')]
    joltages += [current_joltages]


# PART 1: Trying BFS
button_presses = 0
for i in range(len(lights)):
    desired = lights[i]
    current_buttons = buttons[i]
    seen_configs = set()
    seen_configs.add(0)
    presses = 0
    queue = [(0, 0)]
    while len(queue) != 0:
        current_config, steps = queue.pop(0)
        if current_config == desired:
            break
        for button in current_buttons:
            new_config = current_config ^ button
            if new_config not in seen_configs:
                seen_configs.add(new_config)
                queue += [(new_config, steps+1)]
    button_presses += steps

print('Part 1: ' + str(button_presses))

#Part 2.  Use Z3
button_presses = 0
for light in range(len(lights)):
    zsolve = z3.Optimize()
    vars = []

    light_buttons = buttons_raw[light]
    light_jolt = joltages[light]
    jolt_var = [None] * len(light_jolt)

    for i, button in enumerate(light_buttons):
        var = z3.Int(str(i))
        vars += [var]
        zsolve.add(var >= 0)
        for item in button: 
            if jolt_var[item] == None:
                jolt_var[item] = var
            else:
                jolt_var[item] += var
    for index in range(len(light_jolt)):
        if jolt_var[index] != None:
            zsolve.add(light_jolt[index] == jolt_var[index])
    solved = zsolve.minimize(sum(vars))
    if zsolve.check() == z3.sat:
        current_pressed = solved.value().as_long()
    button_presses += current_pressed
print('Part 2: ' + str(button_presses))
