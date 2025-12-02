def load_input():
    with open('../in/in02', 'r') as in_stream:
        return [item_range.split('-') for item_range in in_stream.read().split(',')]

def count_invalid(item_range, part_1):
    start_str, end = item_range
    invalid_sum = 0

    for i in range(int(start_str), int(end) + 1):
        if part_1 and is_invalid_1(str(i)) or not part_1 and is_invalid_2(str(i)):
            invalid_sum += int(i)

    return invalid_sum

def is_invalid_1(s):
    return len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]

def is_invalid_2(s):
    for l in range(1, len(s) // 2 + 1):
        if len(s) % l != 0:
            continue

        if s == ''.join(s[:l] * (len(s) // l)):
            return True
    return False

print(f'Part 1: {sum(count_invalid(item_range, True) for item_range in load_input())}')
print(f'Part 2: {sum(count_invalid(item_range, False) for item_range in load_input())}')