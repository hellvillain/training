# Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

import os

path = 'C:/Users/ashapkin/Documents/Training/PyCh/'


def smart_sorting(filename):
    lift = os.listdir(filename)
    py_line_total_count = 0
    for doc in lift:
        if doc.endswith(".py"):
            opening = open(path + doc, 'r')
            for line in opening:
                if line == '\n':
                    pass
                elif line.startswith('#'):
                    pass
                else:
                    py_line_total_count += 1
    return py_line_total_count

print smart_sorting(path)