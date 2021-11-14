mappings = {
    'U': set(),
    'R': set(('R')),
    'Y': set(('Y')),
    'B': set(('B')),
    'O': set(('R', 'Y')),
    'P': set(('R', 'B')),
    'G': set(('Y', 'B')),
    'A': set(('R', 'Y', 'B')),
}

def solve() -> str:
    input()
    P = [mappings[c] for c in input()]

    last_r = False
    last_y = False
    last_b = False
    total = 0
    for n in P:
        r = 'R' in n
        y = 'Y' in n
        b = 'B' in n
        if r == True and r != last_r:
            total += 1
        if y == True and y != last_y:
            total += 1
        if b == True and b != last_b:
            total += 1
        last_r = r
        last_y = y
        last_b = b

    return total
 
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), solve()))
