### Bonus implementation for part 1 that constructs the invalid ids and only iterates over those.  Much faster but
### doesn't really scale for part 2 so this isn't the real solution file.

def load_input():
    with open('../in/in02', 'r') as in_stream:
        return [item_range.split('-') for item_range in in_stream.read().split(',')]

def count_invalid(item_range):
    start_str, end = item_range
    invalid_sum = 0

    if len(start_str) % 2 == 0:
        current = start_str if is_invalid(start_str) else start_str[:len(start_str)//2] + start_str[:len(start_str)//2]
    else:
        current = get_next_even_len(start_str)

    while int(current) <= int(end):
        if len(current) % 2 == 1:
            current = get_next_even_len(current)
        if int(current) >= int(start_str):
            invalid_sum += int(current)
        current = get_next_invalid(current)

    return invalid_sum

def get_next_even_len(s):
    s = ''.join((['1'] + ['0' for _ in range((len(str(s)) - 1) // 2)]))
    return s + s

def is_invalid(s):
    return len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]

def get_next_invalid(s):
    s2 = str(int(s[:len(s)//2]) + 1)
    s2 += s2
    return s2 if len(s2) == len(s) else get_next_even_len(s2)

print(f'Part 1: {sum(count_invalid(item_range) for item_range in load_input())}')
