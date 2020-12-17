import copy

inputList = []
with open("input.txt") as f:
    inputList = [['.'] + list(x) + ['.'] for x in f.read().split('\n')]
    
paddingList = ['.'] * len(inputList[0])
inputList.insert(0, paddingList)
inputList.append(paddingList)

hasChanged = True
p1Input = copy.deepcopy(inputList)
while hasChanged:
    hasChanged = False
    nextState = copy.deepcopy(p1Input)

    for i, row in enumerate(p1Input[1:-1], 1):
        for j, col in enumerate(row[1:-1], 1):
                           
            adjacent = p1Input[i-1][j-1:j+2] + p1Input[i+1][j-1:j+2] + p1Input[i][j-1:j+2:2]
            if col == 'L' and adjacent.count('#') == 0:
                nextState[i][j] = '#'
                hasChanged = True
            elif col == '#' and adjacent.count('#') >= 4:
                nextState[i][j] = 'L'
                hasChanged = True
                     
    p1Input = nextState.copy()

p1 = 0
for x in p1Input:
    p1 += x.count('#')

# Part 2
def getSeat(row, col, direction, matrix):
    minmaxCol = [0, len(matrix[0])-1]
    minmaxRow = [0, len(matrix)-1]
    
    nextRow = row + direction[0]
    nextCol = col + direction[1]
    adjacentSeat = matrix[nextRow][nextCol]
    
    if adjacentSeat in ['#', 'L'] or nextRow in minmaxRow or nextCol in minmaxCol:
        return adjacentSeat
    else:
        return getSeat(nextRow, nextCol, direction, matrix)

directions = [(0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]

p2Input = copy.deepcopy(inputList)

hasChanged = True
while hasChanged:
    hasChanged = False
    nextState = copy.deepcopy(p2Input)

    for i, row in enumerate(p2Input[1:-1], 1):
        for j, col in enumerate(row[1:-1], 1):
            nrOccupied = 0               
            for direction in directions:
                if getSeat(i, j, direction, p2Input) == '#':
                    nrOccupied += 1
                if nrOccupied == 5:
                    break
            if col == 'L' and  nrOccupied == 0:
                nextState[i][j] = '#'
                hasChanged = True
            elif col == '#' and  nrOccupied >= 5:
                nextState[i][j] = 'L'
                hasChanged = True
                     
    p2Input = nextState.copy()

p2 = 0
for x in p2Input:
    p2 += x.count('#')

print(f"Part one: {p1}")
print(f"Part two: {p2}")
