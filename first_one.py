import tempfile

alist_1 = range(1, 20, 1)
alist_2 = range(1, 20, 1)
alist_3 = range(1, 20, 3)


# 5a. 1, def ver.: making squares from a list of numbers
def squaring(alist):
    return [x**2 for x in alist]

# 5a. 2, lambda ver.:  making squares from a list of numbers
lambda_squaring = lambda alist: [x**2 for x in alist]

# 5b. 1, def ver.: each second element from a list of numbers
def each_second(alist):
    return [x for x in alist if x % 2 == 0]

# 5b. 2, lambda ver.: each second element from a list of numbers
lambda_each_second = lambda alist: [x for x in alist if x % 2 == 0]

# c. 5c: squares of even elements on uneven positions;
def mixed_second(alist):
    return [x**2 for x in alist if x % 2 == 0 and alist.index(x) % 2 != 0]


# d. task 4b: own zip perfomance
def zipping(alist_1, alist_2):
    if len(alist_1) != len(alist_2):
        print "You brought up lists with wrong length"
        return None
    else:
        zipped = ((x,y) for x in alist_1 for y in alist_2 if alist_1.index(x) == alist_2.index(y))
        return list(zipped)


# f. creating cat function
# filepath_one = "C:/Users/Alexis/Documents/Training/Stager/sin.txt"
# filepath_two = "C:/Users/Alexis/Documents/Training/Stager/bread.txt"
# final_destiny = "C:/Users/Alexis/Documents/Training/Stager/vasiliy.txt"


def cat(*args):
    with tempfile.TemporaryFile() as tmp:
        for every in args:
            tmp.writelines(line if '\n' in line else "%s\n" % line for line in open(every, 'r'))
        tmp.seek(0)
        print tmp.read()

# cat(filepath_one, filepath_two)

print "my zip output:", zipping(alist_1, alist_2)
print "original zip output:", zip(alist_1, alist_2)
print "each_second:", each_second(alist_2)
print "mixed:", list(mixed_second(alist_2))
print "lambda_squaring:", lambda_squaring(alist_2)
print "lambda_each_second:", lambda_each_second(alist_2)
