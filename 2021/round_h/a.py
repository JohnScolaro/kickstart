def solve() -> str:
    S = [e for e in input()]
    F = set(f for f in input())

    mappings = {}
    for s in S:
        if s not in mappings:
            min_dif = min(diff(s, f) for f in F)
            mappings[s] = min_dif

    return sum(mappings[s] for s in S)

def diff(s, f):
    diff = abs(ord(s) - ord(f))
    if diff > 13:
        diff -= 2 * (diff - 13)
    return diff
 
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), solve()))
