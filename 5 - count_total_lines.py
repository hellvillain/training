#Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

import os

path = 'C:/Users/ashapkin/Documents/Training/PyCh/'


def total_lines(filename):
    lift = os.listdir(filename)
    py_line_total_count = 0
    for doc in lift:
        if doc.endswith(".py"):
            opening = open(path + doc, 'r')
            for line in opening:
                py_line_total_count += 1
    return py_line_total_count

print total_lines(path)
