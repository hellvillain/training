# Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.
import os

path = 'C:/Users/ashapkin/Documents/Training/PyCh'


def findfiles(filename):
    lift = os.listdir(filename)
    py_file_count = 0
    for doc in lift:
        if doc.endswith(".py"):
            py_file_count += 1
            print doc
    return py_file_count

print findfiles(path)
