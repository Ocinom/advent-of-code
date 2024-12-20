left = []
right = []
res = 0

with open("i1.txt", "r") as f:
    for line in f.readlines():
        num_strs = line.split("   ")
        if len(num_strs) >= 2:
            left.append(int(num_strs[0]))
            right.append(int(num_strs[1]))


for l, r in zip(sorted(left), sorted(right)):
    res += abs(l - r)

print(f"Part 1: {res}")

left_occurences = { num: 0 for num in set(left) }
for r in right:
    if r in left_occurences:
        left_occurences[r] += 1

print(sum(k * v for k, v in left_occurences.items()))
