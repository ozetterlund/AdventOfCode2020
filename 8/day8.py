def runProgram(intructions, findLoop):
    accumulator = 0
    next = 0
    history = set()
    while True:
        history.add(next)
        
        if intructions[next][0] == 'acc':
            accumulator += int(intructions[next][1])
            next += 1
        elif intructions[next][0] == 'jmp':
            next += int(intructions[next][1])
        else:
            next += 1
        
        if (next in history and findLoop) or next >= len(intructions):
            return accumulator
        elif next in history:
            return None

instructions = []
with open("input.txt") as f:
    instructions = [x.split(' ') for x in f.read().split('\n')]

p2 = 0
for i, name in enumerate(instructions):
    instructionsCopy = instructions.copy()
    if name[0] == 'acc':
        continue
    elif name[0] == 'jmp':
        instructionsCopy[i] = 'nop'
    else:
        instructionsCopy[i] = 'jmp'

    p2 = runProgram(instructionsCopy, False)
    
    if p2:
        break

    
print(f"Part one: {runProgram(instructions, True)}")
print(f"Part two: {p2}")
