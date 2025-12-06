import math

def load_and_calculate_input_pt1():
    with open('../in/in06', 'r') as in_stream:
        sums_and_products = [[int(v), int(v)] for v in in_stream.readline().strip().split()]
        operators = None
        for line in in_stream.readlines():
            if line[0] in ['+', '*']:
                operators = line.strip().split()
            else:
                sums_and_products = [[sums_and_products[i][0] + int(v), sums_and_products[i][1] * int(v)] for i, v in enumerate(line.strip().split())]

        return sums_and_products, operators

def load_input2():
    with open('../in/in06', 'r') as in_stream:
        lines = in_stream.readlines()
        return [l for l in lines[:-1]], lines[-1].strip().split()

def build_operands(unparsed_operands):
    problem_operands = []
    current_problem = []
    for c in range(len(unparsed_operands[0])):
        operand = ''.join(([unparsed_operands[r][c] for r in range(len(unparsed_operands))])).strip()
        if len(operand) == 0:
            problem_operands.append(current_problem)
            current_problem = []
        else:
            current_problem.append(operand)

    if len(current_problem) > 0:
        problem_operands.append(current_problem)

    return [[int(v) for v in problem] for problem in problem_operands]

sums_and_products, operators = load_and_calculate_input_pt1()
print('Part 1: ' + str(sum([v[0] if operators[i] == '+' else v[1] for i, v in enumerate(sums_and_products)])))
operands, operators = (lambda _operands, _operators: (build_operands(_operands), _operators))(*load_input2())
print('Part 2: ' + str(sum([sum(v) if operators[i] == '+' else math.prod(v) for i, v in enumerate(operands)])))