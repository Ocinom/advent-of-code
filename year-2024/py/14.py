import re
from PIL import Image
import time

PATTERN = r"-?\d+,-?\d+"
TILE_HEIGHT = 103
TILE_WIDTH = 101
SECONDS = 100

quadrants = {
    "TL": 0,
    "TR": 0,
    "BL": 0,
    "BR": 0,
}

def coords_to_quadrant(x, y):
    bad_horizontal = (TILE_WIDTH - 1) / 2
    bad_vertical = (TILE_HEIGHT - 1) / 2

    if y > bad_vertical:
        if x < bad_horizontal:
            quadrants["BL"] += 1
        elif x > bad_horizontal:
            quadrants["BR"] += 1
    elif y < bad_vertical:
        if x < bad_horizontal:
            quadrants["TL"] += 1
        elif x > bad_horizontal:
            quadrants["TR"] += 1


pos = []
velo = []
found = 0

def plot():
    grid = [['.' for _ in range(TILE_WIDTH)] for _ in range(TILE_HEIGHT)]
    for coord in pos:
        x, y = coord[0], coord[1]
        grid[y][x] = "#"
    return grid


def plot_image(grid):
    img = Image.new( 'RGB', (200, 200) , "white")
    pixels = img.load()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                pixels[i,j] = (0,0,0)
    img.show()

def move():
    for i, (p, v) in enumerate(zip(pos, velo)):
        p_x = (p[0] + v[0]) % TILE_WIDTH
        p_y = (p[1] + v[1]) % TILE_HEIGHT
        pos[i] = [p_x, p_y]

def search(grid) -> bool:
    for line in grid:
        l = ''.join(line)
        if "#####" in l:
            return True
    return False

def print_grid(grid):
    for line in grid:
        print(''.join(line))

with open("i14.txt", "r") as f:
    for line in f.readlines():
        # print(re.findall(PATTERN, line))
        matches = re.findall(PATTERN, line)
        # [px, py]
        p = list(map(int, matches[0].split(',')))
        px, py = p[0], p[1]
        pos.append(p)

        # [vx, vy]
        v = list(map(int, matches[1].split(',')))
        vx, vy = v[0], v[1]
        velo.append(v)

        end_x = (px + (SECONDS * vx)) % TILE_WIDTH
        end_y = (py + (SECONDS * vy)) % TILE_HEIGHT

        coords_to_quadrant(end_x, end_y)

# print(quadrants)
#
# res = 1
# for count in quadrants.values():
#     res *= count
# print(res)

seconds_passed = 0
while True:
    seconds_passed += 1
    print(seconds_passed)
    move()
    g = plot()
    if search(g):
        plot_image(g)
        _ = input("")
    time.sleep(0.001)
