from collections import deque, defaultdict

region_count = defaultdict(int)
regions = defaultdict(set)
region_sides = {}
region_surrounding = {}
map = []

with open("i12.txt", "r") as f:
    for line in f.readlines():
        stripped = line.strip()
        if len(stripped) > 0:
            map.append(list(stripped))


def cardinals(coord: tuple[int,int]) -> list[tuple[int,int]]:
    (y, x) = coord
    return [(y + direction[0], x+ direction[1]) for direction in [
        # Top
        (-1, 0),
        # Bottom
        (1, 0),
        # Left
        (0, -1),
        # Right
        (0, 1),
    ]]


def diagonals(coord: tuple[int,int]) -> list[tuple[int,int]]:
    (y, x) = coord
    return [(y + direction[0], x+ direction[1]) for direction in [
        # Top left
        (-1, -1),
        # Top right
        (-1, 1),
        # Bottom left
        (1, -1),
        # Bottom right
        (1, 1),
    ]]
 

def eight_directions(coord: tuple[int,int]) -> list[tuple[int, int]]:
    (y, x) = coord
    return [(y + direction[0], x+ direction[1]) for direction in [
        # Top left
        (-1, -1),
        # Top right
        (-1, 1),
        # Bottom left
        (1, -1),
        # Bottom right
        (1, 1),
        # Top
        (-1, 0),
        # Bottom
        (1, 0),
        # Left
        (0, -1),
        # Right
        (0, 1),
    ]]

def char_at(coord: tuple[int,int]) -> str:
    return map[coord[0]][coord[1]] if within_bounds(coord) else "*"

def within_bounds(coord: tuple[int,int]) -> bool:
    (y, x) = coord
    return y >= 0 and x >= 0 and y < len(map) and x < len(map[0])

explored = set()
price = 0
for y in range(len(map)):
    for x in range(len(map)):
        if (y, x) in explored:
            continue

        queue = deque([(y, x)])
        ch = map[y][x]

        region_id = ch + str(region_count[ch])
        region_count[ch] += 1
        regions[region_id] = set()

        while queue:
            coord = queue.popleft()
            if coord in regions[region_id]:
                continue
            explored.add(coord)
            regions[region_id].add(coord)

            # Add existing unexplored characters within the same region - in all 4 cardinal directions
            for cardinal in cardinals(coord):
                if within_bounds(cardinal) and map[cardinal[0]][cardinal[1]] == ch:
                    queue.append(cardinal)


for id, coords in regions.items():
    convex_corners = 0
    concave_corners = 0
    for coord in coords:
        ch = char_at(coord)
        cards = cardinals(coord)
        diags = diagonals(coord)

        for diag in diags:
            card_0, card_1 = (coord[0], diag[1]), (diag[0], coord[1])
            char_0 = char_at(card_0)
            char_1 = char_at(card_1)

            if char_0 != ch and char_1 != ch:
                convex_corners += 1
            elif char_0 == ch and char_1 == ch and char_at(diag) != ch:
                concave_corners += 1

    # print(f"Region {id}: Convexes = {convex_corners}, Concaves = {concave_corners}")
    print(f"Region {id}: area = {len(coords)}, sides = {convex_corners + concave_corners}")
    price += len(coords) * (convex_corners + concave_corners)

print(f"Total price: {price}")
# print("842018 TOO HIGH")
# print("830094 TOO LOW")
# print("836056 TOO LOW")
