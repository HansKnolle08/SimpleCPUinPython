"""
/SimpleCPUinPython/src/Helper.py

This module provides helper functions for the Simple CPU emulator,
including a debug function to display the CPU state during execution.

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

#---------#
# IMPORTS #
#---------#
from time import sleep
import sys

# ------------------------#
# CPU STATE VISUALIZATION #
# ------------------------#
def _show_cpu_state(steps, reg_a, reg_b, reg_c, reg_d, reg_res, pc, carry_flag, zero_flag):
    print("=" * 60)
    print(f"STEP: {steps}")
    print("-" * 60)
    print(
        f"A: {reg_a:02X}  "
        f"B: {reg_b:02X}  "
        f"C: {reg_c:02X}  "
        f"D: {reg_d:02X}  "
        f"RES: {reg_res:02X}"
    )
    print(f"PC: {pc:02X}")
    print(f"FLAGS -> CARRY: {int(carry_flag)} | ZERO: {int(zero_flag)}")
    print("=" * 60)

# -----------------------------#
# RAM VISUALIZATION (HEX DUMP) #
# -----------------------------#
def _show_memory_state(ram):
    print("RAM:")
    print("-" * 60)
    for i in range(0, len(ram), 16):
        chunk = ram[i:i + 16]
        hex_values = " ".join(f"{byte:02X}" for byte in chunk)
        print(f"{i:02X} | {hex_values}")
    print("-" * 60)

# --------------------#
# MAIN DEBUG FUNCTION #
# --------------------#
def debug(
    steps,
    max_steps,
    sleep_time,
    reg_a,
    reg_b,
    reg_c,
    reg_d,
    reg_res,
    pc,
    carry_flag,
    zero_flag,
    ram
):
    _show_cpu_state(
        steps,
        reg_a,
        reg_b,
        reg_c,
        reg_d,
        reg_res,
        pc,
        carry_flag,
        zero_flag
    )

    _show_memory_state(ram)

    sleep(sleep_time)

    if steps >= max_steps:
        print("DEBUG: Max steps reached. Stopping execution.")
        sys.exit(0)
