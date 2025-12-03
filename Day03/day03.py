def load_input():
    with open('../in/in03', 'r') as in_stream:
        return [line.strip() for line in in_stream.readlines()]

def get_max_joltage_n(bank, cell_size):
    cell = bank[:cell_size]
    for i in range(cell_size, len(bank)):
        candidate = cell + bank[i]
        pop_idx = next((j for j in range(cell_size) if candidate[j] < candidate[j + 1]), -1)
        cell = candidate[:cell_size] if pop_idx < 0 else candidate[:pop_idx] + candidate[pop_idx + 1:]

    return cell

print(f'Part 1: {sum(int(get_max_joltage_n(bank, 2)) for bank in load_input())}')
print(f'Part 2: {sum(int(get_max_joltage_n(bank, 12)) for bank in load_input())}')