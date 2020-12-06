with open("input.txt") as f:
    groups = f.read().split('\n\n')
    print(sum([len(set(x.replace('\n', ''))) for x in groups]))
    print(sum([len(set.intersection(*list(map(set, x.split('\n'))))) for x in groups]))

