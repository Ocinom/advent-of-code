from collections import deque

trailheads = []
map = []

def integerize(d: str, y, x) -> int:
    if d == '0':
        trailheads.append((0, y, x))
    return int(d)

with open("i10.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        line = line.strip()
        map.append([integerize(d, y, x) for (x, d) in enumerate(line)])


def trailhead_traversal(trailhead: tuple[int,int,int]):
    queue = deque()
    queue.append(trailhead)
    while queue and queue[0][0] != 9:
        (val, y, x) = queue.popleft()

        # Up
        if y > 0 and map[y - 1][x] == val + 1:
            queue.append((val + 1, y - 1, x))
        # Down
        if y < len(map) - 1 and map[y + 1][x] == val + 1:
            queue.append((val + 1, y + 1, x))
        # Left
        if x > 0 and map[y][x - 1] == val + 1:
            queue.append((val + 1, y, x - 1))
        # Right
        if x < len(map[0]) - 1 and map[y][x + 1] == val + 1:
            queue.append((val + 1, y, x + 1))

    return (len(set(queue)), len(queue))

part_one, part_two = 0, 0
for th in trailheads:
    (p1_add, p2_add) = trailhead_traversal(th)
    part_one += p1_add
    part_two += p2_add


print(f"""
Part One: {part_one}
Part Two: {part_two}
""")
