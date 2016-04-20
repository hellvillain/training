# Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import os

path = 'C:/Users/ashapkin/Documents/Training/PyCh/level1.py'


def split_file(filename, n):
    lines_q = n
    outputBase = 'output'
    input = open(filename, 'r')

    count = 0
    file_number = 0
    opening = None
    for line in input:
        if count % lines_q == 0:
            if opening: opening.close()
            opening = open(outputBase + str(file_number) + 'txt', 'w')
            file_number += 1
        opening.write(line)
        count += 1
    return file_number

print split_file(path, 17)
