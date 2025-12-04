def load_input():
    with open('../in/in04', 'r') as in_stream:
        return [list(line.strip()) for line in in_stream.readlines()]

def get_forklift_certified_positions(grid):
    height = len(grid)
    width = len(grid[0])
    certified_papers_pos = []

    tile_pos = [(x, y) for x in range(width) for y in range(height) if grid[y][x] == '@']
    for pos in tile_pos:
        paper_sum = 0
        for x in range(-1 if pos[0] > 0 else 0, 2 if pos[0] < width - 1 else 1):
            for y in range(-1 if pos[1] > 0 else 0, 2 if pos[1] < height - 1 else 1):
                if x == 0 and y == 0:
                    continue
                paper_sum += 1 if grid[pos[1] + y][pos[0] + x] == '@' else 0
        if paper_sum < 4:
            certified_papers_pos.append(pos)

    return certified_papers_pos


def count_removable_papers(grid):
    papers_removed = 0
    papers_to_remove = get_forklift_certified_positions(grid)

    while len(papers_to_remove) > 0:
        papers_removed += len(papers_to_remove)
        for pos in papers_to_remove:
            grid[pos[1]][pos[0]] = '.'
        papers_to_remove = get_forklift_certified_positions(grid)

    return papers_removed

print(f'Part 1: {len(get_forklift_certified_positions(load_input()))}')
print(f'Part 2: {count_removable_papers(load_input())}')