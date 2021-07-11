from collections import defaultdict

def solve() -> str:
    N, C = [int(e) for e in input().split()]
    intervals = []
    for _ in range(N):
        split_input = input().split()
        intervals.append((int(split_input[0]), int(split_input[1])))

    # Build up dict
    strings_per_cut = defaultdict(int)
    for x in intervals:
        strings_per_cut[x[0] + 1] += 1
        strings_per_cut[x[1]] -= 1

    # Remove zeros
    strings_per_cut = [(a, b) for a, b in strings_per_cut.items() if b != 0]
    strings_per_cut.sort(key=lambda x: x[0])

    # Create dict of num_extra_strings: num_cuts_that_yeild
    d = defaultdict(int)
    cum_extra_strings = 0
    cur_string_loc = 0
    for i in strings_per_cut:
        # Finding num cuts
        num_cuts = i[0] - cur_string_loc
        d[cum_extra_strings] += num_cuts

        # Getting read for next iter
        cur_string_loc = i[0]
        cum_extra_strings += i[1]

    num_cuts_yeilding_extra_cuts = [(a, b) for a, b in d.items() if a != 0]
    num_cuts_yeilding_extra_cuts.sort(key=lambda x: x[0], reverse=True)

    initial_intervals = len(intervals)
    extra_intervals = 0
    remaining_cuts = C
    for cut_group in num_cuts_yeilding_extra_cuts:
        if remaining_cuts > cut_group[1]:
            extra_intervals += cut_group[0] * cut_group[1]
            remaining_cuts -= cut_group[1]
        else:
            extra_intervals += remaining_cuts * cut_group[0]
            break

    return initial_intervals + extra_intervals
 
T = int(input())
 
for t in range(1, T + 1):
    print ("Case #{}: {}".format(str(t), solve()))
