#!/usr/bin/python3
"""
"5-text_indentation" module.

"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each ".", "?" and ":"

        Argd:
            text (str): string to be indented
    """


    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
