import itertools
import os

alist = range(1, 20, 1)
alist_2 = range(1, 20, 1)
alist_3 = range(1, 20, 3)


# a. making squares from a list of numbers
def squaring (list):
    alist = [x**2 for x in list]
    return alist


# b. making squares for each second from a list of numbers
def each_second (list):
    alist = [x for x in list if x%2 != 0]
    return alist


# c. squares of even elements on uneven positions;
def mixed_second (list):
    alist = [x**2 for x in list if x%2 == 0 and list.index(x)%3 == 0]
    return alist


# d. own zip perfomance
def zipping(alist_1, alist_2):
    if len(alist_1) != len(alist_2):
        print "You brought up lists with wrong length"
    else:
        zipped = [x*y for x in alist_1 for y in alist_2 if alist_1.index(x)==alist_2.index(y)]
        return zipped


# f. creating cat function
filepath_one = "C:/Users/ashapkin/Documents/Training/sin.txt"
filepath_two = "C:/Users/ashapkin/Documents/Training/bread.txt"
final_destiny = "C:/Users/ashapkin/Documents/Training/vasiliy.txt"


def cat(*args):
    with tempfile.TemporaryFile() as tmp:
        for every in args:
            tmp.writelines(line if '\n' in line else "%s\n" % line for line in open(every, 'r'))
        tmp.seek(0)
        print tmp.read()

cat(filepath_one, filepath_two)

b = [4 for x in range(1,10,2)]

print b
print squaring(alist)
print each_second(alist)
print mixed_second(alist)
print my_chain(alist, alist_2)
print zipping(alist, alist_2)
