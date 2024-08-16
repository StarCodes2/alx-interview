#!/usr/bin/python3
"""
    Defines a script that reads stdin line by line and computes metrics.
"""
import re
import signal
import sys

total_size = 0
code_count = {}


def regex_check(line: str) -> bool:
    """ Checks if a string matches a regex expression. """
    regex = (r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
             r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
    return re.match(regex, line)


def display_stat(code_count: dict, size: int) -> None:
    """ Print the processed logs. """
    print("File size: {}".format(size))
    for key in sorted(code_count.keys()):
        print("{}: {}".format(key, code_count[key]))


def sig_handler(signum, frame):
    """ Handles the CTRL + c keyboard interrupt. """
    display_stat(code_count, total_size)
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)


def main() -> None:
    """ Reads in input stdin line by line, process it and print them. """
    global total_size
    global code_count
    try:
        line_count = 0

        for line in sys.stdin:
            line = line.strip()
            line_count += 1

            if not regex_check(line):
                continue
            try:
                line_list = line.split()
                size = int(line_list[-1])
                status = int(line_list[-2])

                total_size += size
                if status in code_count:
                    code_count[status] += 1
                else:
                    code_count[status] = 1

                if line_count % 10 == 0:
                    display_stat(code_count, total_size)
            except ValueError:
                continue

    except KeyboardInterrupt:
        display_stat(code_count, total_size)
        sys.exit(0)

    if line_count % 10 != 0:
        display_stat(code_count, total_size)


if __name__ == "__main__":
    main()
