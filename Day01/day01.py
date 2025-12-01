def load_input():
    with open('../in/in01', 'r') as in_stream:
        return [[line[0].strip(), int(line[1:].strip())] for line in in_stream.readlines()]


def count_zeroes(start, turns, count_clicks):
    zeroes = 0
    last_pos, pos = start, start
    for turn in turns:
        if turn[1] == 0:
            continue

        sign = 1 if turn[0] == 'R' else -1
        pos += sign * turn[1]
        dz = 0
        if count_clicks:
            dz = abs(pos // 100 - last_pos//100)
            # Handle edge cases that appear when moving left
            if turn[0] == 'L':
                if pos % 100 == 0: # If moving onto a multiple of 100, we will not see the transition
                    dz += 1
                if last_pos % 100 == 0: # If moving off of a multiple of 100, we will have an extra transition
                    dz -= 1
        elif pos % 100 == 0:
            dz = 1
        zeroes += dz
        last_pos = pos

    return zeroes

print(f'Part 1: {count_zeroes(50, load_input(), False)}')
print(f'Part 2: {count_zeroes(50, load_input(), True)}')