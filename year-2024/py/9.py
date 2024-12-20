from collections import deque
from visualizer import *

# Part 1
digits = deque()
empties = deque()

# Part 2
# A slot always has some or no amount of empty space next to it
# 
slots = []
res = deque()

with open("i9.txt", "r") as f:
    line = f.readlines()[0].strip()
    # counter = 1
    # digits.append((0, int(line[0])))
    # slots.append(deque([(0, int(line[0]))]))
    # for i in range(1, len(line), 2):
    #     digits.append((counter, int(line[i + 1])))
    #     slots.append(deque([(counter, int(line[i + 1]))]))
    #     empties.append(int(line[i]))
    #     counter += 1

    id = 0
    empty = False
    for digit in line:
        if empty:
            empties.append(int(digit))
            empty = False
        else:
            digits.append((id, int(digit)))
            slots.append(deque([(id, int(digit))]))
            id += 1
            empty = True
        

# Copy empties for part 2 as it will be mutated for part 1
empties_c = empties.copy()


# digits @ y = 0
# empties @ y = 1
# res @ y = 2
# def fresh_matrix() -> TwoDMatrix:
#     return TwoDMatrix([digits, empties, res], tick=0.5)

while digits and empties:
    if digits:
        # mat = fresh_matrix()
        # mat.add_action_set([mat.set_color], [{"y": 2, "x": 0, "new_color": Color.BRIGHT_RED}])
        leftmost = digits.popleft()
        res.append(leftmost)

        # mat.animate()

    if empties:
        e = empties.popleft()
        while e > 0:
            if not digits:
                break
            last = digits.pop()
            if e < last[1]:
                digits.append((last[0], last[1] - e))
                res.append((last[0], e))
                e = 0
            else:
                e = e - last[1]
                res.append(last)


tot = 0
ctr = 0
for nums in res:
    digit = nums[0]
    for _ in range(nums[1]):
        tot += digit * ctr
        ctr += 1

print(f"Part One: {tot}")

# mat.animate()

empties = empties_c
for idx in range(len(slots) - 1, 0, -1):
    file_to_move = slots[idx][0]
    file_size = file_to_move[1]
    for e_idx in range(idx):
        if empties[e_idx] >= file_size:
            slots[e_idx].append(file_to_move)
            empties[e_idx] -= file_size
            empties[idx - 1] += file_size
            slots[idx].popleft()
            break


tot = 0
ctr = 0
last_non_empty = 50000
result_str = ""
for i in range(len(slots) - 1, -1, -1):
    if len(slots[i]) > 0:
        last_non_empty = i + 1
        break

for i in range(last_non_empty):
    slot = slots[i]
    empty_count = empties[i]
    for (num, count) in slot:
        for _ in range(count):
            result_str += str(num)
            tot += ctr * num
            ctr += 1
    ctr += empty_count
    result_str += '.' * empty_count

print(f"Part Two: {tot}")
