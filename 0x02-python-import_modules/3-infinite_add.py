#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    #convert arguments to integers and calculate sum
    total = sum(int(arg) for arg in arguments)
    #print total
    print(total)
