import  bisect

seats = []
with open("input.txt") as f:
    seats = [x.strip() for x in f.readlines()]

higestId = 0
ids = []
for seat in seats:
    row = int('0b'+seat[:7].replace('F', '0').replace('B', '1'), 2)
    col = int('0b'+seat[7:].replace('L', '0').replace('R', '1'), 2)
    
    # Part 1
    currentId = row*8+col
    if currentId > higestId:
        higestId = currentId
        
    # Part 2
    bisect.insort(ids, currentId)

i = 0
myId = None
while True:
    if (ids[i] + 1) != ids[i+1]:
        myId = ids[i] + 1
        break
    i += 1

print(f"Part one: {higestId}")
print(f"Part two: {myId}")
