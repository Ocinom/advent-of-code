# <test value>: ...Operators
from collections import deque

# Part 2
def concat(l: int, r: int) -> int:
    digits = []
    while r > 0:
        r, rem = divmod(r, 10)
        digits.append(rem)

    for d in digits[::-1]:
        l *= 10
        l += d

    return l

def calibrate(test_value: int, nums: list[int]) -> bool:

    nums = nums[::-1]
    queue = deque()
    queue.append(nums.pop())


    while nums:
        next = nums.pop()
        for _ in range(len(queue)):
            element = queue.popleft()
            # Part 1
            if element + next <= test_value:
                queue.append(element + next)
            if element * next <= test_value:
                queue.append(element * next)

            # Part 2
            if concat(element, next) <= test_value:
                queue.append(concat(element, next))

    return test_value in queue


found = set()
with open("i7.txt", "r") as f:
    for line in f.readlines():
        if len(line) == 0:
            continue
        split_test_value = line.split(":")
        test_value = int(split_test_value[0])
        nums = list(map(int, split_test_value[1].strip().split(" ")))

        if calibrate(test_value, nums):
            found.add(test_value)

print(sum(found))
