"""
/SimpleCPUinPython/src/CPUMain.py

A simple CPU emulator in Python with basic ALU and control flow instructions, 
supporting debugging and step-by-step execution.

MIT License

Copyright (c) 2026 Hansisi
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

###########
# IMPORTS #
###########
from Helper import debug
import os

##################
# CPU MAIN CLASS #
##################
class CPU:
    def __init__(self):
        # General-Purpose Registers
        self.reg_a: int = 0
        self.reg_b: int = 0
        self.reg_c: int = 0
        self.reg_d: int = 0

        # Result Register
        self.reg_res: int = 0

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
            'JNZ': self.instr_jnz,
            'JC': self.instr_jc,
            'JNC': self.instr_jnc,
            'PRINT': self.instr_print
        }

        # Labels for jumps
        self.labels: dict[str, int] = {}

    ####################
    # ALU INSTRUCTIONS #
    ####################

    # ADD Instruction: ADD reg1 reg2 -> reg_res = reg1 + reg2
    def instr_add(self, instr):
        _, reg1, reg2 = instr.split()
        val1 = getattr(self, f"reg_{reg1.lower()}")
        val2 = getattr(self, f"reg_{reg2.lower()}")

        result = val1 + val2
        self.carry_flag = result > 0xFF
        self.reg_res = result & 0xFF
        self.zero_flag = (self.reg_res == 0)

    # SUB Instruction: SUB reg1 reg2 -> reg_res = reg1 - reg2
    def instr_sub(self, instr):
        _, reg1, reg2 = instr.split()
        val1 = getattr(self, f"reg_{reg1.lower()}")
        val2 = getattr(self, f"reg_{reg2.lower()}")

        result = val1 - val2
        self.carry_flag = result < 0
        self.reg_res = result & 0xFF
        self.zero_flag = (self.reg_res == 0)

    # MUL Instruction: MUL reg1 reg2 -> reg_res = reg1 * reg2
    def instr_mul(self, instr):
        _, reg1, reg2 = instr.split()
        val1 = getattr(self, f"reg_{reg1.lower()}")
        val2 = getattr(self, f"reg_{reg2.lower()}")

        result = val1 * val2
        self.carry_flag = result > 0xFF
        self.reg_res = result & 0xFF
        self.zero_flag = (self.reg_res == 0)

    # DIV Instruction: DIV reg1 reg2 -> reg_res = reg1 // reg2
    def instr_div(self, instr):
        _, reg1, reg2 = instr.split()
        val1 = getattr(self, f"reg_{reg1.lower()}")
        val2 = getattr(self, f"reg_{reg2.lower()}")

        if val2 == 0:
            raise ZeroDivisionError(f"Division durch 0 ({reg1} / {reg2})")

        self.reg_res = val1 // val2
        self.zero_flag = (self.reg_res == 0)
    
    ######################
    # LOGIC INSTRUCTIONS #
    ######################

    # JMP Instruction: JMP target -> PC = target
    def instr_jmp(self, instr):
        _, target = instr.split()
        if target in self.labels:
            self.pc = self.labels[target]
        else:
            self.pc = int(target)

    # JZ Instruction: JZ target -> if zero_flag: PC = target
    def instr_jz(self, instr):
        _, target = instr.split()
        if self.zero_flag:
            if target in self.labels:
                self.pc = self.labels[target]
            else:
                self.pc = int(target)

    # JNZ Instruction: JNZ target -> if not zero_flag: PC = target
    def instr_jnz(self, instr):
        _, target = instr.split()
        if not self.zero_flag:
            if target in self.labels:
                self.pc = self.labels[target]
            else:
                self.pc = int(target)

    # JC Instruction: JC target -> if carry_flag: PC = target
    def instr_jc(self, instr):
        _, target = instr.split()
        if self.carry_flag:
            if target in self.labels:
                self.pc = self.labels[target]
            else:
                self.pc = int(target)

    # JNC Instruction: JNC target -> if not carry_flag: PC = target
    def instr_jnc(self, instr):
        _, target = instr.split()
        if not self.carry_flag:
            if target in self.labels:
                self.pc = self.labels[target]
            else:
                self.pc = int(target)

    # LOAD Instruction: LOAD value target -> target = value (value can be immediate or register)
    def instr_load(self, instr):
        _, value, target = instr.split()

        target_reg = f"reg_{target.lower()}"
        if not hasattr(self, target_reg):
            raise ValueError(f"Register {target_reg} doesn't exist")

        if hasattr(self, f"reg_{value.lower()}"):
            source_value = getattr(self, f"reg_{value.lower()}")
        else:
            source_value = int(value)

        setattr(self, target_reg, source_value)

    # PRINT Instruction: PRINT reg -> prints the value of the specified register
    def instr_print(self, instr):
        _, flagged = instr.split()
        flagged_reg = f"reg_{flagged.lower()}"
        value = getattr(self, flagged_reg)
        print(f"{flagged_reg.upper()} = {value}")

    #############
    # EXECUTION #
    #############

    # Load a program into memory
    def load_program(self, program):
        self.memory = program
        self.pc = 0

    # Execute a single instruction
    def step(self):
        instr = self.memory[self.pc]
        self.pc += 1

        opcode = instr.split()[0]
        self.instr_reg[opcode](instr)

    # Run the CPU until the end of the program or until max_steps is reached
    def execute(self, debug_state: bool = True, max_steps: int = 1000, sleep_time: int = 0):
        try:
            steps = 0
            while self.pc < len(self.memory):
                self.step()
                steps += 1
                if debug_state:
                    debug(
                        steps, 
                        max_steps, 
                        sleep_time, 
                        self.reg_a, 
                        self.reg_b, 
                        self.reg_c, 
                        self.reg_d,
                        self.reg_res,
                        self.pc, 
                        self.carry_flag, 
                        self.zero_flag
                    )
        except KeyboardInterrupt:
            print("Processing stopped by user")
