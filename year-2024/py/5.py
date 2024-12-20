from collections import defaultdict

bad_befores = defaultdict(list)
right_order_middle_pages = []
wrong_orders = []

with open("i5.txt", "r") as f:
    for line in f.readlines():
        if "|" in line:
            # 47|53 => [47,53]
            bb_entry = list(map(int, line.split("|")))
            bad_befores[bb_entry[1]].append(bb_entry[0])

        if "," in line:
            nums = list(map(int, line.split(",")))
            bbs = set()
            right_order = True
            for num in nums:
                if num in bbs:
                    right_order = False
                    wrong_orders.append(nums)
                    break
                for bad_num in bad_befores[num]:
                    bbs.add(bad_num)

            if right_order:
                right_order_middle_pages.append(int(nums[len(nums) // 2]))


print(sum(right_order_middle_pages))

res = 0
for order in wrong_orders:
    filtered_befores = {
        num: [k for k in bad_befores[num] if k in order] for num in order
    }
    sorted_keys = sorted(filtered_befores.keys(), key=lambda x: len(filtered_befores[x]))
    res += sorted_keys[len(sorted_keys) // 2]

print(res)
