import re
from typing import Callable


class Computer:


    def __init__(self, A=0, B=0, C=0) -> None:
        self.A = A
        self.B = B
        self.C = C
        self.instruction_ptr = 0
        self.output = []
        self.program = []
        self.OPCODE = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def read_program(self):
        while self.instruction_ptr < len(self.program):
            

    def print_output(self):
        print(self.output)

    def opcode(self, code: int) -> Callable:
        return self.OPCODE[code]

    def combo(self, operand) -> int:
        res = 0
        match operand:
            case literal if literal in [0,1,2,3]:
                res = literal
            case 4:
                res = self.A
            case 5:
                res = self.B
            case 6:
                res = self.C
            case _:
                pass
        return res

    def adv(self, operand):
        combo = self.combo(operand)
        self.A = int(self.A / 2**combo)

    def bxl(self, operand):
        self.B ^= operand

    def bst(self, operand):
        combo = self.combo(operand)
        self.B = combo % 8

    def jnz(self, operand) -> int|None:
        if self.A != 0:
            return operand

    def bxc(self, operand):
        self.B ^= self.C

    def out(self, operand):
        combo = self.combo(operand)
        self.output.append(combo % 8)

    def bdv(self, operand):
        combo = self.combo(operand)
        self.B = int(self.A / 2**combo)

    def cdv(self, operand):
        combo = self.combo(operand)
        self.C = int(self.A / 2**combo)

    @staticmethod
    def load_program(input: list[str]):
        computer = Computer()
        for line in input:
            if "A" in line:
                val = re.search(r'\d+', line)
                computer.A = int(val[0])
            elif "B" in line:
                val = re.search(r'\d+', line)
                computer.B = int(val[0])
            elif "C" in line:
                val = re.search(r'\d+', line)
                computer.C = int(val[0])
            elif "Program" in line:
                start = re.search(r"\d", line).start()
                prog= list(map(int, line[start:].strip().split(",")))
                program = []
                for p in range(0, len(prog), 2):
                    program.append((prog[p], prog[p + 1]))
                computer.program = program
        return computer
    
    def __str__(self) -> str:
        return f"Computer ( A: {self.A}, B: {self.B}, C: {self.C}, Prog: {self.program} )"


test = None
with open("i17_test.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    test = Computer.load_program(lines)

test.read_program()
test.print_output()
