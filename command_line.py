import sys

from convert import str_to_float


def command_line_sums(finders : list[str])  -> float:
    total = 0.0
    for finder in finders:
        num = str_to_float(finder)
        if num is not None:
            total += num
    return total

def do_sum(args : str) -> float:
    l = args.split(" ")
    return command_line_sums(l)


if __name__ == '__main__':
    full = sys.argv[1:]
    print(command_line_sums(full))
