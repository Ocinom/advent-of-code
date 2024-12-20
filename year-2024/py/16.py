import heapq
import soln_for_16 as soln
import sys
from enum import Enum
from collections import deque
import copy


class dirs(Enum):
    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)

    def opposite(self):
        match self:
            case self.up:
                return self.down
            case self.down:
                return self.up
            case self.left:
                return self.right
            case self.right:
                return self.left
            case _:
                raise ValueError("IDIOT")

    def __gt__(self, other):
        return self.value > other.value
    
    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

grid = []
start, end = (-1,-1), (-1,-1)

with open("i16.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        grid.append([])
        for x, ch in enumerate(line):
            grid[y].append(ch)
            if ch == "E":
                end = (y, x)
            if ch == "S":
                start = (y, x)

if start == (-1,-1) or end == (-1,-1):
    raise ValueError("IMPOSSIBLE")


def part_one():
    start_y, start_x = start
    from_start = {(start_y, start_x, dirs.right.value): 0}
    queue = []
    heapq.heappush(queue, (0, start_y, start_x, dirs.right))
    while queue:
        cost, y, x, direction = heapq.heappop(queue)
        if (y, x) == end:
            from_start[(y, x, direction.value)] = cost
            return from_start

        for dir in dirs:
            next_y, next_x = y + dir.value[0], x + dir.value[1]
            if grid[next_y][next_x] != "#":
                if dir == direction:
                    new_cost = cost + 1
                else:
                    new_cost = cost + 1000
                    next_y, next_x = y, x

                if (next_y, next_x, dir.value) not in from_start or new_cost < from_start[(next_y, next_x, dir.value)]:
                    heapq.heappush(queue, (new_cost, next_y, next_x, dir))
                    from_start[(next_y, next_x, dir.value)] = new_cost

    return from_start

def part_two():
    end_y, end_x = end
    queue = []
    from_end = {}
    for dir in dirs:
        heapq.heappush(queue, (0, end_y, end_x, dir))

    while queue:
        cost, y, x, direction = heapq.heappop(queue)

        if (y, x, direction.value) not in from_end or cost < from_end[(y, x, direction.value)]:
            from_end[(y, x, direction.value)] = cost

        for dir in dirs:
            next_y, next_x = y + dir.value[0], x + dir.value[1]
            if grid[next_y][next_x] != "#":
                if dir == direction:
                    new_cost = cost + 1
                else:
                    new_cost = cost + 1000
                    next_y, next_x = y, x

                if (next_y, next_x, dir.value) not in from_end:
                    heapq.heappush(queue, (new_cost, next_y, next_x, dir))


    return from_end


from_start_matrix = part_one()

min_cost = -1
for dir in dirs:
    end_entry = (end[0], end[1], dir.value)
    if end_entry in from_start_matrix:
        min_cost = from_start_matrix[end_entry]

# print(f"Part 1: {min_cost}")

from_end_matrix = part_two()

# for e in from_end_matrix:
#     if e[0] == 139:
#         print(f"e val: {e}")

seats = set()
tot = 0
for entry in from_end_matrix:
    y, x, dir = entry
    cost = from_end_matrix[entry]
    opposite_dir = (dir[0] * -1, dir[1] * -1)
    if (y, x, opposite_dir) in from_start_matrix and cost + from_start_matrix[(y, x, opposite_dir)] == min_cost:
        tot += 1
        seats.add((y, x))

print(f"Part Two: {len(seats)}")

result_set = soln.part2(soln.parse(open("i16.txt").readlines()))
for item in result_set:
    (y, x) = item
    if item not in seats:
        print(f"ITEM: {item}")
        grid[y][x] = '\033[91mO\033[35m'
    else:
        grid[y][x] = '\033[96mO\033[35m'



for line in grid:
    print()
    sys.stdout.write("".join(line).strip() + "\r")
