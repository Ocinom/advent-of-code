from collections import defaultdict
from itertools import combinations
from visualizer import *

node_coords = defaultdict(list)
map = []
antinodes = set()


def within_bounds(y, x):
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])

with open("i8.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        map.append(list(line.strip()))
        for x, ch in enumerate(line):
            if ch != '.' and ch != '\n':
                node_coords[ch].append((y, x))

mat = TwoDMatrix(map, tick=0.05)

for ch, coords in node_coords.items():
    coord_combos = list(combinations(coords, 2))
    if len(coord_combos) < 2:
        continue
    for combo in coord_combos:
        # dx, dy = xa - xb, ya - yb
        # c = (ya + dy, xa + dx)
        # d = (yb - dy, xb - dx)
        ya, xa = combo[0][0], combo[0][1]
        yb, xb = combo[1][0], combo[1][1]
        dy, dx = ya - yb, xa - xb

        c = (ya, xa)
        d = (yb, xb)
        antinodes.add(c)
        antinodes.add(d)

        c_params = {
            "y": ya,
            "x": xa,
            "new_color": Color.BRIGHT_RED,
        }
        d_params = {
            "y": yb,
            "x": xb,
            "new_color": Color.BRIGHT_RED,
        }

        line_points = [c, d]

        mat.add_action_set([mat.set_color, mat.set_color], [c_params, d_params])
        while (c := (c[0] + dy, c[1] + dx)) and within_bounds(c[0],c[1]):
            line_points.append(c)
            y = c[0]
            x = c[1]
            if map[y][x] == ".":
                params = {
                    "y": y,
                    "x": x,
                    "new_elem": "#",
                    "new_color": Color.BRIGHT_BLUE,
                }
                mat.add_action_set([mat.set_colored_elem], [params])
            antinodes.add((y,x))
        while (d := (d[0] - dy, d[1] - dx)) and within_bounds(d[0],d[1]):
            line_points.append(d)
            y = d[0]
            x = d[1]
            if map[y][x] == ".":
                params = {
                    "y": y,
                    "x": x,
                    "new_elem": "#",
                    "new_color": Color.BRIGHT_BLUE,
                }
                mat.add_action_set([mat.set_colored_elem], [params])
            antinodes.add((y,x))

        actions = [mat.set_color for _ in range(len(line_points))]
        params = []
        for coord in line_points:
            param = {
                "y": coord[0],
                "x": coord[1],
                "new_color": Color.BRIGHT_GREEN,
            }
            params.append(param)
        mat.add_action_set(actions, params)

mat.animate()

print(len(antinodes))

