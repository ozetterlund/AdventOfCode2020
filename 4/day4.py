import re

inputList = []
with open("input.txt") as f:
    inputList = f.read().split('\n\n')
    for i in range(len(inputList)):
        inputList[i] = inputList[i].replace('\n',' ').split(' ')

inputDictList = []
for input in inputList:
    inputDict = {}
    for entry in input:
        key, val = entry.split(':')
        inputDict[key] = val
        
    inputDictList.append(inputDict)

# Part 1

validPassports = 0

for passport in inputDictList:
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
        validPassports += 1

print(f"Part one: {validPassports}")

# Part 2

def checkbyr(year):
    return 1920 <= int(year) <= 2002
def checkiyr(year):
    return 2010 <= int(year) <= 2020
def checkeyr(year):
    return 2020 <= int(year) <= 2030
def checkhgt(hgt):
    x = re.search("(^1([5-8][0-9]|9[0-3])cm$)|(^(59|6[0-9]|7[0-6])in$)", hgt)
    return bool(x)
def checkhcl(hcl):
    x = re.search("^#[0-9a-f]{6}$", hcl)
    return bool(x)
def checkecl(color):
    return color in ['amb','blu','brn','gry','grn','hzl','oth']
def checkpid(pid):
    x = re.search("^[0-9]{9}$", pid)
    return bool(x)
    
validPassports = 0
for passport in inputDictList:
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
        if (checkbyr(passport['byr']) and 
        checkiyr(passport['iyr']) and 
        checkeyr(passport['eyr']) and 
        checkhgt(passport['hgt']) and 
        checkhcl(passport['hcl']) and
        checkecl(passport['ecl']) and
        checkpid(passport['pid'])):
            validPassports += 1

print(f"Part two: {validPassports}")

