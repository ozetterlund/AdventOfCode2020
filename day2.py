
inputList = []
with open(r"Inputs\input2.txt") as f:
    inputList = [line.strip().split() for line in f]

# Part 1
numValids = 0
for password in inputList:
    limits = password[0].split('-')
    lowLim = int(limits[0])
    highLim = int(limits[1])
    letter = password[1][0]
    occurence = password[2].count(letter)
    
    if occurence >= lowLim and occurence <= highLim:
        numValids += 1

print("Part one: " + str(numValids))

# Part 2
    
numValids = 0
for passwordList in inputList:
    limits = passwordList[0].split('-')
    first = int(limits[0])
    second = int(limits[1])
    letter = passwordList[1][0]    
    password = passwordList[2]
    
    if bool(password[first-1] == letter) ^ bool(password[second-1] == letter):
        numValids += 1

print("Part two: " + str(numValids))

