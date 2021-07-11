from collections import defaultdict

def solve() -> str:
    a, b, c = [int(e) for e in input().split()]
    d, e = [int(e) for e in input().split()]
    f, g, h = [int(e) for e in input().split()]

    def ave(a, b):
        round_error = (a + b) % 2
        if round_error:
            return None
        return (a + b) // 2 
    
    hard_sets = [(a, b, c), (a, d, f), (c, e, h), (f, g, h)]
    soft_sets = [(a, h), (b, g), (d, e), (f, c)]
    
    num_hard_sets = 0
    for i, j, k in hard_sets:
        if ave(i, k) == j:
            num_hard_sets += 1

    x = defaultdict(int)
    for i, j in soft_sets:
        v = ave(i, j)
        if v is not None:
            x[v] += 1
    if len(x) == 0:
        x = {0:0}

    num_soft_sets = max(x.values())
    return num_hard_sets + num_soft_sets
    
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), solve()))
