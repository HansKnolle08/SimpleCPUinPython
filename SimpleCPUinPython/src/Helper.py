from time import sleep

def _show_cpu_state(steps, reg_a, reg_b, reg_c, reg_d, reg_res, prog_cnt, carry_flag, zero_flag):
    print(f"Step {steps}: A={reg_a} B={reg_b} C={reg_c} D={reg_d} RES={reg_res} PC={prog_cnt} CarryFlag={carry_flag} ZeroFlag={zero_flag}")

def debug(steps, max_steps, sleep_time, reg_a, reg_b, reg_c, reg_d, reg_res, prog_cnt, carry_flag, zero_flag):
    _show_cpu_state(steps, reg_a, reg_b, reg_c, reg_d, reg_res, prog_cnt, carry_flag, zero_flag)
    sleep(sleep_time)
    if steps >= max_steps:
        print("Debug: Max steps reached, stopping run.")
        return 0