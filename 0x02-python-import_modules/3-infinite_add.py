#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    total = sum(int(arg) for arg in (arguments))
    print(total)
