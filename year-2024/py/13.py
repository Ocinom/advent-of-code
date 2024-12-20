import numpy as np
import re

A_COST = 3
B_COST = 1

class Machine:

    def __init__(self, a: tuple[int,int], b: tuple[int,int], prize: tuple[int,int]) -> None:
        self.a = a
        self.b = b
        self.prize = prize

    def solve(self) -> tuple[int,int]:
        a_pushes = -1
        b_pushes = -1
        b_push = 0
        while self.b[0] * b_push < self.prize[0] and self.b[1] * b_push < self.prize[1]:
            b_x = self.b[0] * b_push
            b_y = self.b[1] * b_push

            x_dist = self.prize[0] - b_x
            y_dist = self.prize[1] - b_y

            p_x = x_dist / self.a[0]
            p_y = y_dist / self.a[1]
            if p_x == p_y and int(p_x) == p_x:
                a_pushes = int(p_x)
                b_pushes = b_push

            b_push += 1

        return (-1, -1) if a_pushes < 0 or b_pushes < 0 else (a_pushes, b_pushes)

    def solve_2(self) -> tuple[int,int]:
        left_side = np.array([[self.a[0], self.b[0]], [self.a[1], self.b[1]]])
        right_side = np.array([self.prize[0] + 10000000000000, self.prize[1] + 10000000000000])
        x = np.round(np.linalg.solve(left_side, right_side), 3)
        if x[0].is_integer() and x[1].is_integer():
            return (int(x[0]), int(x[1]))
        else:
            return (-1, -1)

total = 0
with open("i13.txt", "r") as f:
    a, b, prize = (-1, -1), (-1, -1), (-1, -1)
    for line in f.readlines():
        if len(line.strip()) > 0:
            vals = re.findall(r"\d+", line)
            if len(vals) != 2:
                print("SOMETHING WENT HORRIBLY WRONG!")
                print(vals)
            coords = (int(vals[0]), int(vals[1]))
            if "A" in line:
                a = coords
            elif "B" in line:
                b = coords
            elif "P" in line:
                m = Machine(a, b, coords)
                soln = m.solve_2()
                print(soln)
                if soln[0] > 0:
                    total += soln[0] * A_COST + soln[1] * B_COST

print(total)
