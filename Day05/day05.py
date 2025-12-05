def load_input():
    with open('../in/in05', 'r') as in_stream:
        lines = in_stream.readlines()
        divider_idx = lines.index('\n')
        return sorted([tuple(map(int, line.strip().split('-'))) for line in lines[:divider_idx]], key=lambda pair: pair[0]), [int(line.strip()) for line in lines[divider_idx + 1:]]

def merge_ranges(fresh_ranges):
    ranges = [fresh_ranges[0]]
    for rng in fresh_ranges[1:]:
        latest = ranges[-1]
        if latest[0] <= rng[0] <= latest[1]:
            ranges[-1] = (ranges[-1][0], max(ranges[-1][1], rng[1]))
        else:
            ranges.append(rng)

    return ranges

merged_ranges, candidates = (lambda _ranges, _candidates: (merge_ranges(_ranges), _candidates))(*load_input())
print(f'Part 1: {len([c for c in candidates if any(r for r in merged_ranges if r[0] <= c <= r[1])])}')
print(f'Part 2: {sum([v[1] - v[0] + 1 for v in merged_ranges])}')