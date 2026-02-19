from CPUMain import CPU

def main(debug_mode: bool = False):
    cpu = CPU()

    cpu.load_program([
        'LOAD 150 A',
        'LOAD 1 B',
        'ADD',
        'PRINT C'
    ])

    cpu.run(debug_mode)

if __name__ == '__main__':
    main(True)