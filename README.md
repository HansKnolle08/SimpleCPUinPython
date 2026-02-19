
# SimpleCPUinPython
-------------------

A lightweight CPU emulator written in Python that simulates basic processor operations including arithmetic logic unit (ALU) instructions and control flow.

## Features
-----------

- **General-Purpose Registers**: A, B, C, D with a dedicated result register
- **ALU Instructions**: ADD, SUB, MUL, DIV
- **Control Flow**: JMP, JZ, JNZ, JC, JNC (conditional jumps based on flags)
- **Memory Operations**: LOAD and PRINT instructions
- **Status Flags**: Carry and Zero flags for conditional branching
- **Debug Mode**: Step-by-step execution with real-time CPU state visualization
- **Program Loading**: Load programs from `.scp` assembly files with label support

## Quick Start
--------------

```python
from CPUMain import CPU
from ASMParser import ASMParser

cpu = CPU()
parser = ASMParser()

program, labels = parser.parse_file('Programs/label_test.scp')

cpu.labels = labels
cpu.load_program(program)
cpu.execute()
```

## Example Program
------------------

```assembly
MOV 3 A
LOAD 5 B
ADD A B
PRINT RES
```

## Instruction Set
------------------

| Instruction | Description |
|---|---|
| `LOAD value/register register` | Load new value into a register or value of other register into a register|
| `ADD reg1 reg2` | Add two registers, store in RES |
| `SUB reg1 reg2` | Subtract reg2 from reg1 |
| `MUL reg1 reg2` | Multiply two registers |
| `DIV reg1 reg2` | Divide reg1 by reg2 |
| `JMP target` | Jump to address |
| `JZ/JNZ target` | Jump if zero/not zero flag set |
| `JC/JNC target` | Jump if carry/no carry flag set |
| `PRINT register` | Output register value |

## License
----------

MIT License - See LICENSE file for details
