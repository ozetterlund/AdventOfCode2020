from itertools import combinations

preamble = 25

input = []
with open("input.txt") as f:
    input = [int(x) for x in f.read().split('\n')]

p1 = 0
for i, num in enumerate(input[preamble:], preamble):
    if num not in [sum(x) for x in combinations(input[i-preamble:i], 2)]:
        p1 = num

p2 = 0
for i in range(0, len(input)):
    i2 = i + 1
    
    x = 0    
    while x < p1:
        i2 += 1
        x = sum(input[i:i2])
    
    if x == p1:
        p2 = min(input[i:i2]) + max(input[i:i2])
        break

print(f"Part one: {p1}")
print(f"Part two: {p2}")
