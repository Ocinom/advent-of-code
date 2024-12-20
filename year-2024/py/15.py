from collections import deque
import os
import time

grid = []
commands = ""
start = [0,0]
TICK = 0.005

with open("i15.txt", "r") as f:
    command_flag = False
    for y, line in enumerate(f.readlines()):
        stripped = line.strip()
        if len(stripped) == 0:
            command_flag = True
            continue
        if command_flag:
            commands += stripped
            continue
        grid.append([])
        for x, ch in enumerate(stripped):
            match ch:
                case "#":
                    grid[y].append("#")
                    # For part 2
                    grid[y].append("#")
                case "O":
                    # append "O" for part 1
                    grid[y].append("[")
                    grid[y].append("]")
                case "@":
                    start = (y, len(grid[y]))
                    grid[y].append("@")
                    grid[y].append(".")
                case ".":
                    grid[y].append(".")
                    grid[y].append(".")
                case _:
                    break

dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

def print_grid():
    for line in grid:
        print("".join(line))

def move_p1(dir: tuple[int,int], y, x):
    """
    Place an "O" at the end, move the "@" symbol once in the direction and place a "." in its original place
    """
    global start
    next_y, next_x = y + dir[0], x + dir[1]
    while grid[next_y][next_x] == "O":
        next_y, next_x = next_y + dir[0], next_x + dir[1]

    if grid[next_y][next_x] == ".":
        grid[next_y][next_x] = "O"
        grid[y][x] = "."
        grid[y + dir[0]][x + dir[1]] = "@"
        start = (y + dir[0], x + dir[1])


def p2_move_horizontal(dir: tuple[int,int], y, x):
    """
    Move to the end. If it is a dot, there is an empty space to move into.
    Now just translate each character by 1 in dir's direction - moving from the "." to "@"
    """
    global start

    # Vertical portion is always 0 for horizontals
    horizontal_dir = dir[1]

    next_x = x + horizontal_dir
    while grid[y][next_x] != "#" and grid[y][next_x] != ".":
        next_x += horizontal_dir

    if grid[y][next_x] == ".":
        for ix in range(next_x, x, -horizontal_dir):
            grid[y][ix] = grid[y][ix - horizontal_dir]

        start = [y, x + horizontal_dir]
        grid[y][x] = "."


def p2_move_vertical(dir: tuple[int,int],  y, x):
    """
    Peek the next row in the direction. If there are boxes, add them to the queue. If we hit a wall, we don't push.
    If all end boxes have been peeked and they are all dots, move each character by 1 in dir's direction - starting
    from end edge boxes
    """
    global start
    move_queue = set()
    peek_queue = deque()
    peek_queue.append((y, x))
    while peek_queue:
        next_peek = peek_queue.popleft()
        char_ahead = (next_peek[0] + dir[0], next_peek[1])

        match grid[char_ahead[0]][char_ahead[1]]:
            case "]":
                peek_queue.append((char_ahead[0], char_ahead[1]))
                peek_queue.append((char_ahead[0], char_ahead[1] - 1))
            case "[":
                peek_queue.append((char_ahead[0], char_ahead[1]))
                peek_queue.append((char_ahead[0], char_ahead[1] + 1))
            case "#":
                return
        move_queue.add(next_peek)

    to_move = sorted(list(move_queue), key=lambda x: x[0], reverse=dir[0] > 0)
    for position in to_move:
        next_y = position[0] + dir[0]
        pos_x = position[1]
        grid[next_y][pos_x] = grid[position[0]][position[1]]
        grid[position[0]][position[1]] = "."

    start = (y + dir[0], x)

def move_p2(command: str, y, x):
    dir = dirs[command]
    if command == "<" or command == ">":
        p2_move_horizontal(dir, y, x)
    else:
        p2_move_vertical(dir, y, x)

command_length = len(commands)
start_flag = False
for s, command in enumerate(commands):
    print(f"Moves: {s + 1}/{command_length}")
    print_grid()
    if not start_flag:
        _ = input("Above is the starting board. Press 'Enter' to start the animation.")
        start_flag = True
    move_p2(command, start[0], start[1])
    time.sleep(TICK)
    # cls if on Windows - Linux user btw.
    os.system("clear")

res = 0
for y, line in enumerate(grid):
    for x, ch in enumerate(line):
        if ch == "[":
            res += 100 * y + x
print(res)
