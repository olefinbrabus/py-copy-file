def copy_file(command: str) -> None:

    s_command = command.split()
    if not command or s_command[0] != "cp":
        return

    try:
        f_file, s_file = s_command[1], s_command[2]
    except IndexError:
        return

    if f_file == s_file:
        return
    try:
        with open(f_file, "r") as f_in, open(s_file, "w") as f_out:
            for line in f_in:
                f_out.write(line)
    except FileNotFoundError:
        return
