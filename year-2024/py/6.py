start = [0,0]
map = []

with open("i6.txt", "r") as f:
    row = 0
    for line in f.readlines():
        if "^" in line:
            start = [row, line.index("^")]
        map.append(line.strip())
        row += 1

# up: -1, 0
# right: 0, 1
# down: 1, 0
# left: 0, -1
directions = [
    #up
    [-1, 0],
    # right
    [0, 1],
    # down,
    [1, 0],
    # left
    [0, -1]
]

def at_edge(y, x) -> bool:
    return y == 0 or x == 0 or y == len(map) - 1 or x == len(map[0]) - 1

# y, x
visited = set()

visited_with_direction = set()

current_direction = 0
loops = []

dir_strs = {
    0: "^",
    1: ">",
    2: "v",
    3: "<"
}

def replace_char_in_string(s, ch, idx) -> str:
    return s[:idx] + ch + s[idx + 1:]

loops = 0
y, x = start[0], start[1]
while not at_edge(y, x):
    # y direction is at 0, x direction is at 1 
    visited.add((y, x))

    next_y = y + directions[current_direction][0]
    next_x = x + directions[current_direction][1]

    if map[next_y][next_x] == "#":
            current_direction = (current_direction + 1) % len(directions)
            next_y = y + directions[current_direction][0]
            next_x = x + directions[current_direction][1]

    y, x, = next_y, next_x

else:
    visited.add((y, x))


if (start[0], start[1]) in visited:
    visited.remove((start[0], start[1]))

def infinite_walk(new_map) -> bool:
    y, x = start[0], start[1]
    dir = 0
    v = set()
    v.add((y, x, dir))

    while not at_edge(y, x):

        next_y = y + directions[dir][0]
        next_x = x + directions[dir][1]

        if new_map[next_y][next_x] == "#":
            dir = (dir + 1) % len(directions)
        else:
            y, x = next_y, next_x

        if (y, x, dir) in v:
            return True
        v.add((y, x, dir))

    return False

infinite_walks = 0
for entry in visited:
    map_copy = map.copy()
    block_y, block_x = entry[0], entry[1]
    map_copy[block_y] = replace_char_in_string(map_copy[block_y], "#", block_x)
    if infinite_walk(map_copy):
        infinite_walks += 1

print(len(visited))
print(loops)
print(infinite_walks)
# for loop in loops:
#     map[loop[0]] = map[loop[0]][:loop[1]] + "P" + map[loop[0]][loop[1] + 1:]

# for line in map:
#     if len(line.strip()) > 0:
#         print(line)
