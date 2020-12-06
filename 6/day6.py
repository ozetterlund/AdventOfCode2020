import string

alphabet = set(string.ascii_lowercase)
p1 = p2 = 0
with open("input.txt") as f:
    groups = f.read().split('\n\n')
    p1 = sum([len(set(x.replace('\n', ''))) for x in groups])
    p2 = sum([len(alphabet.intersection(*list(map(set, x.split('\n'))))) for x in groups])

print(f"Part one: {p1}")
print(f"Part two: {p2}")
