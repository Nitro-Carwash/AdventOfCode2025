import math

def load_input():
    with open('../in/in08', 'r') as in_stream:
        return [list(line.strip().split(',')) for line in in_stream.readlines()]

def find_circuits(points, stop_after_it_count, it_count):
    # build a list of edges between every point, sorted ascending by dist^2
    # tuple is (dist, v1, v2)
    edges = sorted([(dist2(pair[0], pair[1]), pair[0], pair[1]) for pair in [(points[i], points[j]) for i in range(len(points)) for j in range(i+1, len(points))]], key=lambda edge: edge[0])

    # dictionary mapping vertices to the list of every other vertex sharing its circuit.  Each list of circuits is a shared ref
    v_to_circuit = {}
    last_added_boxes = None
    it = 0
    largest_circuit_size = 0

    while (stop_after_it_count and it < it_count) or (not stop_after_it_count and largest_circuit_size < len(points)):
        it += 1
        if it % 1000 == 0:
            print(f'Reached iteration: {it}')

        _, v1, v2 = edges.pop(0)

        # stringify the point tuple so that it can be used as a dict key
        v1 = ','.join(v1)
        v2 = ','.join(v2)

        if v1 in v_to_circuit and v2 in v_to_circuit:
            # merge them if necessary.  keep in mind that each circuit list (value) is a shared reference
            if v_to_circuit[v1] != v_to_circuit[v2]:
                v_to_circuit[v1] += v_to_circuit[v2]
                # update the references in the joined list
                for v in v_to_circuit[v2]:
                    v_to_circuit[v] = v_to_circuit[v1]
            else:
                continue
        elif v1 in v_to_circuit:
            v_to_circuit[v1].append(v2)
            v_to_circuit[v2] = v_to_circuit[v1]
        elif v2 in v_to_circuit:
            v_to_circuit[v2].append(v1)
            v_to_circuit[v1] = v_to_circuit[v2]
        else:
            v_to_circuit[v1] = [v1, v2]
            v_to_circuit[v2] = v_to_circuit[v1]

        largest_circuit_size = max(largest_circuit_size, len(v_to_circuit[v1]))
        last_added_boxes = (v1, v2)

    if stop_after_it_count:
        # since we have a bunch of duplicate lists, this ugly list comprehension uses a set to get only the distinct circuits
        # it has to do weird string join and split in order to be compatible with the set which cannot hash lists
        return sorted([s.split('|') for s in list(set('|'.join(c) for c in v_to_circuit.values()))], key=lambda circuit: -len(circuit))[:3]
    else:
        return [box.split(',') for box in last_added_boxes]

def dist2(v1, v2):
    return sum([(int(v1[i]) - int(v2[i]))**2 for i in range(len(v1))])

print(f'{math.prod(len(circuit) for circuit in find_circuits(load_input(), True, 1000))}')
print(f'{math.prod(int(box[0]) for box in  find_circuits(load_input(), False, -1))}')