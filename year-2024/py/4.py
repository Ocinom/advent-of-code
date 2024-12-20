lines = []

with open("i4.txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

res = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "X":
            # Peek Left - SAMX
            if x > 2 and lines[y][x-3:x+1] == "SAMX":
                res += 1
            # Peek Right - XMAS
            if x < len(lines[0]) - 3 and lines[y][x:x+4] == "XMAS":
                res += 1
            # Peek Down ( you get the idea. )
            if y < len(lines) - 3 and "".join(lines[y + a][x] for a in range(4)) == "XMAS":
                res += 1
            # Peek Up
            if y > 2 and "".join(lines[y - a][x] for a in range(4)) == "XMAS":
                res += 1

            # Top Left
            if x > 2 and y > 2 and "".join(lines[y - a][x - a] for a in range(4)) == "XMAS":
                res += 1
            # Top Right 
            if x < len(lines[0]) - 3 and y > 2 and "".join(lines[y - a][x + a] for a in range(4)) == "XMAS":
                res += 1
            # Bottom Left
            if x > 2 and y < len(lines) - 3 and "".join(lines[y + a][x - a] for a in range(4)) == "XMAS":
                res += 1
            # Bottom Right
            if x < len(lines[0]) - 3 and y < len(lines) - 3 and "".join(lines[y + a][x + a] for a in range(4)) == "XMAS":
                res += 1

print(res)

res2 = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        if lines[y][x] == "A":
            # If statement checks are done in this order: top left, top right, bottom left, bottom right

            # M   M
            #   A
            # S   S
            if lines[y - 1][x - 1] == "M" and lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S" and lines[y + 1][x + 1] == "S":
                res2 += 1

            # S   S
            #   A
            # M   M
            if lines[y - 1][x - 1] == "S" and lines[y - 1][x + 1] == "S" and lines[y + 1][x - 1] == "M" and lines[y + 1][x + 1] == "M":
                res2 += 1

            # M   S
            #   A
            # M   S
            if lines[y - 1][x - 1] == "M" and lines[y - 1][x + 1] == "S" and lines[y + 1][x - 1] == "M" and lines[y + 1][x + 1] == "S":
                res2 += 1

            # S   M
            #   A
            # S   M
            if lines[y - 1][x - 1] == "S" and lines[y - 1][x + 1] == "M" and lines[y + 1][x - 1] == "S" and lines[y + 1][x + 1] == "M":
                res2 += 1

print(res2)
