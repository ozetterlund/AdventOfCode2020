
def checkGoldenBags(color):
    if bagsDict[color][0] == '?':
        retVal = ''
        for x in bagsDict[color][1]:
            retVal = checkGoldenBags(x[2:])
            if retVal == 'Y':
                break
        bagsDict[color][0] = retVal
        return retVal
    else:
        return bagsDict[color][0]

def countBags(color, counter):
    if bagsDict[color][2]:
        return bagsDict[color][2]
    else:
        retVal = 0
        for x in bagsDict[color][1]:
            retVal += int(x[0])+int(x[0])*countBags(x[2:], counter)
        return retVal

bags = []
with open("input.txt") as f:
    bags = [x.strip().split(' contain ') for x in f.readlines()]

bagsDict = {}
for bag in bags:
    color = bag[0].replace(' bags', '')
    inside = bag[1].replace(' bags', '').replace(' bag', '').replace('.', '')
    if bag[1] == 'no other bags.':
        bagsDict[color] = ['N', [], 0]
    elif 'shiny gold bag' in bag[1]:
        bagsDict[color] = ['Y', inside.split(', '), None]
    else:
        bagsDict[color] = ['?', inside.split(', '), None]

p1 = 0
for x in bagsDict:
    checkGoldenBags(x)
    if bagsDict[x][0] == 'Y':
        p1 += 1
   
p2 = countBags('shiny gold', 0)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
