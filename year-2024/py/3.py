import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

pattern_2_2 = r"do\(\)"

with open("i3.txt", "r") as f:
    res = re.findall(pattern, f.read())
    print(sum([int(a)*int(b) for a, b in res]))

sum_2 = 0
with open("i3.txt", "r") as f:
    text = "do()" + f.read()
    res = re.split(r"don't\(\)", text)
    for r in res:
        try:
            i = r.index("do()")
            for a, b in re.findall(pattern, r[i:]):
                sum_2 += int(a)*int(b)

        except ValueError:
            pass

print(sum_2)
