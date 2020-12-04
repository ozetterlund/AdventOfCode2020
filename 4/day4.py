import re

passports = []
with open("input.txt") as f:
    passports = f.read().split('\n\n')

p1 = p2 = 0
fields = {'iyr': lambda x: 2010 <= int(x) <= 2020,
          'eyr': lambda x: 2020 <= int(x) <= 2030,
          'hcl': lambda x: bool(re.search("^#[0-9a-f]{6}$", x)),
          'byr': lambda x: 1920 <= int(x) <= 2002,
          'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
          'hgt': lambda x: bool(re.search("(^1([5-8][0-9]|9[0-3])cm$)|(^(59|6[0-9]|7[0-6])in$)", x)),
          'pid': lambda x: bool(re.search("^[0-9]{9}$", x))}

for passport in passports:
    pDict = dict(x.split(':') for x in passport.replace('\n', ' ').split(' '))
    if all([x in pDict for x in fields.keys()]):
        p1 += 1
        pDict.pop('cid', None)
        if all([fields[x](pDict[x]) for x in pDict]):
            p2 += 1

print(f"Part one: {p1}")
print(f"Part two: {p2}")
