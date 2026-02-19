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

###########
# IMPORTS #
###########
from time import sleep
import sys

# Helper function to display the current state of the CPU for debugging purposes
def _show_cpu_state(steps, reg_a, reg_b, reg_c, reg_d, reg_res, prog_cnt, carry_flag, zero_flag):
    print(f"Step {steps}: A={reg_a} B={reg_b} C={reg_c} D={reg_d} RES={reg_res} PC={prog_cnt} CarryFlag={carry_flag} ZeroFlag={zero_flag}")

# Debug function to be called during CPU execution to show the current state and optionally stop after a certain number of steps
def debug(steps, max_steps, sleep_time, reg_a, reg_b, reg_c, reg_d, reg_res, prog_cnt, carry_flag, zero_flag):
    _show_cpu_state(steps, reg_a, reg_b, reg_c, reg_d, reg_res, prog_cnt, carry_flag, zero_flag)
    sleep(sleep_time)
    if steps >= max_steps:
        print("Debug: Max steps reached, stopping run.")
        sys.exit(0)
