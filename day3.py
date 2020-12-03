
inputList = []
with open(r"Inputs\input3.txt") as f:
    inputList = [line.strip() for line in f]

def slopeChecker(slopeList, columnJump, rowJump):
    numOfTrees = 0
    column = 0
    size = len(slopeList[0])
    
    for row in slopeList[rowJump::rowJump]:
        column += columnJump    
        if row[column % size] == '#':
            numOfTrees += 1
    
    return numOfTrees

# Part 1

print("Part one: " + str(slopeChecker(inputList, 3, 1)))

# Part 2

answer2 = slopeChecker(inputList, 1,1)*slopeChecker(inputList, 3,1)*slopeChecker(inputList, 5,1)*slopeChecker(inputList, 7,1)*slopeChecker(inputList, 1,2)
    
print("Part two: " + str(answer2))

