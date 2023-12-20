#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        ans = a / b
    except (ZeroDivisionError, FloatingPointError):
        ans = None
    finally:
        print("Inside results: {}".format(ans))
    return (ans)
