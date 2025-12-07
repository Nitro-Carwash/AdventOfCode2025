def load_input():
    with open('../in/in07', 'r') as in_stream:
        return [list(line.strip()) for line in in_stream.readlines()]

def calculate_splits(grid):
    beam_indices = [0] * len(grid[0])
    split_count = 0
    beam_indices[grid[0].index('S')] = 1

    for row in grid[1:]:
        next_beam_indices = [0] * len(grid[0])
        for col in range(len(row)):
            if row[col] != '^':
                next_beam_indices[col] += beam_indices[col]
            elif beam_indices[col] > 0:
                if col > 0:
                    next_beam_indices[col - 1] += beam_indices[col]
                if col < len(grid[0]) - 1:
                    next_beam_indices[col + 1] += beam_indices[col]
                next_beam_indices[col] = 0
                split_count += 1
        beam_indices = next_beam_indices

    return f'{split_count} | {sum(beam_indices)}'

print(f'Part 1 | Part 2:     {calculate_splits(load_input())}')