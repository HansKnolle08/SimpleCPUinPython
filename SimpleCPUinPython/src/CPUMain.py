class CPU:
    def __init__(self):
        # Registers
        self.reg_a: int = 0
        self.reg_b: int = 0
        self.reg_c: int = 0

        # Program Counter
        self.pc: int = 0

        # Memory
        self.memory: list[str] = []

        # Instruction Register
        self.instr_reg: dict = {
            'ADD': self.instr_add,
            'SUB': self.instr_sub,
            'MUL': self.instr_mul,
            'DIV': self.instr_div,
            'LOAD': self.instr_load,
            'JMP': self.instr_jmp,
            'PRINT': self.instr_print
        }

    # -------- INSTRUCTION IMPLEMENTATIONS --------
    def instr_add(self, _):
        self.reg_c = self.reg_a + self.reg_b

    def instr_sub(self, _):
        self.reg_c = self.reg_a - self.reg_b

    def instr_mul(self, _):
        self.reg_c = self.reg_a * self.reg_b
       
    def instr_div(self, _):
        if self.reg_b == 0:
            raise ZeroDivisionError("Value of reg_b is 0. Division by 0 is undefined")
        
        self.reg_c = self.reg_a // self.reg_b
    
    def instr_jmp(self, instr):
        _, target = instr.split()
        self.pc = int(target)

    def instr_load(self, instr):
        _, value, target = instr.split()
        target_reg = f"reg_{target.lower()}"
        
        if value == 'C':
            setattr(self, target_reg, self.reg_c)   # Ziel = C Registerwert
        else:
            setattr(self, target_reg, int(value))   # Ziel = Immediate Value

    def instr_print(self, instr):
        _, flagged = instr.split()
        flagged_reg = f"reg_{flagged.lower()}"
        value = getattr(self, flagged_reg)
        print(f"{flagged_reg.upper()} = {value}")

    # -------- EXECUTION --------

    def load_program(self, program):
        self.memory = program
        self.pc = 0

    def step(self):
        instr = self.memory[self.pc]
        self.pc += 1

        opcode = instr.split()[0]
        self.instr_reg[opcode](instr)

    def run(self, debug_state: bool = True, max_steps: int = 100):
        try:
            steps = 0
            while self.pc < len(self.memory):
                self.step()
                steps += 1

                if debug_state:
                    print(f"Step {steps}: A={self.reg_a} B={self.reg_b} C={self.reg_c} PC={self.pc}")
                    if steps >= max_steps:
                        print("Debug: Max steps reached, stopping run.")
                        break
        except KeyboardInterrupt:
            print("Processing stopped by user")


# ------- TEST ------- #
cpu = CPU()

cpu.load_program([
    'LOAD 5 A',
    'LOAD 1 B',
    'ADD',
    'LOAD C A',
    'PRINT C',
    'JMP 2',
])

cpu.run()