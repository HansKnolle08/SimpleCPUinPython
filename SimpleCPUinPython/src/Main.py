from CPUMain import CPU

def main(debug_mode: bool = False):
    cpu = CPU()

    cpu.load_program_from_file('Programs/Test.scp')

    cpu.run(debug_mode, sleep_time=0.25)

if __name__ == '__main__':
    main(True)