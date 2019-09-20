#!/usr/bin/python3

from sys import argv as argv
from secrets import choice


def generate_brackets_string():
    return "".join([choice("{}[]()") for x in range(6)])


def check_brackets(input_string=None):
    if len(input_string) % 2 != 0:
        return print(input_string, False)
    else:
        brackets = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        inv_brack = {v: k for k, v in brackets.items()}
        stack = []
        for char in input_string:
            if char in brackets.keys():
                stack.append(char)
            else:
                try:
                    if char in inv_brack.keys() and inv_brack[char] == stack[-1]:
                        stack.pop()
                    else:
                        break
                except:
                    pass
        return print(input_string, not bool(stack), stack)

if __name__ == '__main__':
    if len(argv) > 1:
        check_brackets("".join(argv[1:]))
    else:
        check_brackets(generate_brackets_string())
