class CPU:
    def __init__(self):
        self.reg_a = 0
        self.reg_b = 0
        self.pc = 0
        self.memory = []

    def load_program(self, program):
        self.memory = program
        self.pc = 0

    def step(self):
        instr = self.memory[self.pc]
        self.pc += 1

        if instr == 'ADD':
            self.reg_a += self.reg_b
        elif instr == 'PRINT':
            print("Reg_A =", self.reg_a)


# ------- TEST ------- #
cpu = CPU()
cpu.reg_a = 5
cpu.reg_b = 3
cpu.load_program(['ADD', 'PRINT'])

cpu.step()
cpu.step()