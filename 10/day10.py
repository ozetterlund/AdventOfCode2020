import os

inputList = []
inputpath = os.path.dirname(__file__) + "\input.txt"
with open(inputpath) as f:
    inputList = sorted([int(x) for x in f.read().split('\n')])
    
inputList = [0] + inputList + [max(inputList)+3]

oneJolt = 0
threeJolt = 0
for i in range(0, len(inputList) - 1):
    diff = inputList[i+1] - inputList[i]
    
    if diff == 1:
        oneJolt += 1
    elif diff == 3:
        threeJolt += 1

p1 = oneJolt * threeJolt

print(f"Part one: {p1}")

# Part 2
x = 0
x1 = x2 = x3 = 1
if inputList[-1] - inputList[-3] <= 3:
    x1 = 2

for i, val in reversed(list(enumerate(inputList[:-3]))):
    x = 0
    if inputList[i+1] - val <= 3:
        x += x1
    if inputList[i+2] - val <= 3:
        x += x2
    if inputList[i+3] - val <= 3:
        x += x3
    x3 = x2
    x2 = x1
    x1 = x

print(f"Part two: {x}")
