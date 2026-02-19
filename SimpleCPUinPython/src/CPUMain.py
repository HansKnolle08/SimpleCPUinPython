from Helper import debug

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

        # Flags
        self.carry_flag: bool = False
        self.zero_flag: bool = False

        # Instruction Register
        self.instr_reg: dict = {
            'ADD': self.instr_add,
            'SUB': self.instr_sub,
            'MUL': self.instr_mul,
            'DIV': self.instr_div,
            'LOAD': self.instr_load,
            'JMP': self.instr_jmp,
            'JZ': self.instr_jz,
            'PRINT': self.instr_print
        }

    # -------- ALU INSTRUCTIONS --------
    def instr_add(self, _):
        result = self.reg_a + self.reg_b
        self.carry_flag = result > 0xFF
        self.reg_c = result & 0xFF
        self.zero_flag = (self.reg_c == 0)

    def instr_sub(self, _):
        result = self.reg_a - self.reg_b
        self.reg_c = result & 0xFF
        self.zero_flag = (self.reg_c == 0)
        self.carry_flag = result < 0

    def instr_mul(self, _):
        result = self.reg_a * self.reg_b
        self.carry_flag = result > 0xFF
        self.reg_c = result & 0xFF
        self.zero_flag = (self.reg_c == 0)
       
    def instr_div(self, _):
        if self.reg_b == 0:
            raise ZeroDivisionError("Value of reg_b is 0. Division by 0 is undefined")
        
        self.reg_c = self.reg_a // self.reg_b
        self.zero_flag = (self.reg_c == 0)
    
    # -------- LOGIC INSTRUCTIONS --------
    def instr_jmp(self, instr):
        _, target = instr.split()
        self.pc = int(target)

    def instr_jz(self, instr):
        _, target = instr.split()
        if self.zero_flag:
            self.pc = int(target)

    def instr_load(self, instr):
        _, value, target = instr.split()
        target_reg = f"reg_{target.lower()}"
        
        if value == 'C':
            setattr(self, target_reg, self.reg_c)
        else:
            setattr(self, target_reg, int(value))

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

    def run(self, debug_state: bool = True, max_steps: int = 100, sleep_time: int = 0):
        try:
            steps = 0
            while self.pc < len(self.memory):
                self.step()
                steps += 1
                if debug_state:
                    debug(steps, max_steps, sleep_time, self.reg_a, self.reg_b, self.reg_c, self.pc, self.carry_flag, self.zero_flag)
        except KeyboardInterrupt:
            print("Processing stopped by user")
