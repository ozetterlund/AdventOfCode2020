# Part 1
inputList = []
with open("input1.txt") as f:
    inputList = [int(line.strip()) for line in f]

for i in inputList:
    if 2020 - i  in inputList:
        print((2020 - i)*i) 
        break

# Part 2
def mult3(inList):
    for ind, name in enumerate(inList[:-1]):
        for j, name2 in enumerate(inList[ind+1:]):
            if j+name < 2020:
                for k in inList[j:]:
                    if name+name2+k == 2020:
                        print(name*name2*k)
                        return 

mult3(inputList)
