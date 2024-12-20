def is_safe(l: list[int], s=None) -> int:
    sign = l[1] - l[0] > 0 if s is None else s

    for i in range(1, len(l)):
        diff = l[i] - l[i - 1]
        match sign:
            # positive
            case True:
                if diff < 1 or diff > 3:
                    return 0
            # negative
            case False:
                if diff > -1 or diff < -3:
                    return 0

    return 1

def is_safe_2(l: list[int]) -> bool:
    safepos = set([1,2,3])
    safeneg = set([-1,-2,-3])
    for i in range(1, len(l)):
        safepos.add(l[i] - l[i - 1])
        safeneg.add(l[i] - l[i - 1])

    return len(safepos) <= 4 or len(safeneg) <= 3

with open("i2.txt", "r") as f:
    print(sum([ 
        is_safe([int(ns) for ns in line.split(" ")])
        for line in f.readlines()
    ]))

with open("i2.txt", "r") as f:
    acc = 0
    for line in f.readlines():
        if is_safe_2(list(map(int, line.split(" ")))):
            acc += 1

    print(acc)
