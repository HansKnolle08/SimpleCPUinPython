"""
/SimpleCPUinPython/src/ASMParser.py

A simple assembler parser for the Simple CPU emulator in Python.
It reads assembly code from a file, processes labels, and prepares the program for execution.

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
import os

###############
# ASM PARSER #
###############
class ASMParser:
    def __init__(self):
        self.labels = {}
        self.program = []

    # Parses an assembly file and extracts the program and labels
    def parse_file(self, filename: str):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, filename)

        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue

                line = line.split(';', 1)[0].strip()
                if not line:
                    continue

                if line.endswith(':'):
                    label_name = line[:-1].strip()
                    self.labels[label_name] = len(self.program)
                else:
                    self.program.append(line)

        return self.program, self.labels
