#Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os.path

def findfiles(filename):
    lift = os.listdir(filename)
    for every in lift:
        print every
    return

path = 'C:/Users/ashapkin/Documents/Training/Google Python Class/Google Solutions/google-python-exercises/babynames/'

print findfiles(path)


