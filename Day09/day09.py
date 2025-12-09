import math

def load_input():
    with open('../in/in09', 'r') as in_stream:
        return [[int(v) for v in line.strip().split(',')] for line in in_stream.readlines()]

def area(p1, p2):
    return math.prod([abs(int(p1[i]) - int(p2[i])) + 1 for i in range(len(p1))])

### Checks if the rectangle defined by (p1, p2) is intersected by the edge defined by (e1, e2)
### Specifically, this is where the edge contains some points outside the rectangle
### i.e. merely overlapping is not necessarily an intersection
def intersects_edge(p1, p2, e1, e2):
    rect_x_min, rect_x_max = sorted([p1[0], p2[0]])
    rect_y_min, rect_y_max = sorted([p1[1], p2[1]])
    edge_x_min, edge_x_max = sorted([e1[0], e2[0]])
    edge_y_min, edge_y_max = sorted([e1[1], e2[1]])

    # Since this edge is axis-aligned, the edge points on the edge are only different on one axis.
    # So this check doubles as "Are you within bounds of this rect on the unchanging axis" and
    # "Are you extending out of bounds of this rect on the changing axis"
    return rect_x_min < edge_x_max and rect_x_max > edge_x_min and rect_y_min < edge_y_max and rect_y_max > edge_y_min

def find_largest_red_green_area(points, pairs):
    # Build the green-tile edges and then find the maximum red-tile area that can be constructed without intersecting any of these edges

    edges = []
    for i in range(1, len(points)):
        edges.append((points[i - 1], points[i]))
    edges.append((points[-1], points[0]))

    max_area = 0
    for pair in pairs:
        if not any(edge for edge in edges if intersects_edge(pair[0], pair[1], edge[0], edge[1])):
            max_area = max(max_area, area(pair[0], pair[1]))

    return max_area

points = load_input()
pairs = [pair for pair in [(points[i], points[j]) for i in range(len(points)) for j in range(i + 1, len(points))]]
print(f'Part 1: {max(area(p1, p2) for p1, p2 in pairs)}')
print(f'Part 2: {find_largest_red_green_area(points, pairs)}')
