from collections import defaultdict


def number_of_digits(n: int) -> int:
    res = 0

    while n > 0:
        n //= 10
        res += 1
    return res

def split_digits(n: int) -> tuple[int,int]:
    n_digits = number_of_digits(n)

    right = 0
    exponent = 0
    for _ in range(n_digits // 2):
        right += (n % 10) * 10 ** exponent
        n //= 10
        exponent += 1
    return (int(n), int(right))

def num_produces(n: int) -> dict:
    if n == 0:
        return {1: 1}
    elif number_of_digits(n) % 2 == 0:
        (left, right) = split_digits(n)
        return {left: 2} if left == right else {left: 1, right: 1}
    else:
        return {n*2024: 1}

def dict_pretty_print(d: list[tuple[int, int]]):
    print("{")
    for (k, v) in d:
        print(f"\t{k}: {v},")
    print("}")

    
nums = []
with open("i11.txt", "r") as f:
    line = f.readline()
    vals = map(int, line.split(" "))
    for val in vals:
        nums.append(val)

stones = {}
produces = defaultdict(dict)

# nums = [0]
for num in nums:
    stones[num] = 1
for _ in range(75):
    next = {}
    for key in stones.keys():
        if key not in produces:
            produces[key] = num_produces(key)
        for k, v in produces[key].items():
            # e.g. if one zero produces a '1', then two zeros produce two '1's etc.
            if k not in next:
                next[k] = v * stones[key]
            else:
                next[k] += v * stones[key]
    stones = next

print(sum(stones.values()))
