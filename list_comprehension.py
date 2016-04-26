alist_1 = range(1, 20, 1)
alist_2 = range(1, 20, 1)
alist_3 = range(1, 20, 3)


# 5a, 1, def ver.: making squares from a list of numbers
def squaring(alist):
    return [x**2 for x in alist]

# 5a, 2, lambda ver.:  making squares from a list of numbers
lambda_squaring = lambda alist: [x**2 for x in alist]

# 5b, 1, def ver.: each second element from a list of numbers
def each_second(alist):
    return [x for x in alist if x % 2 == 0]

# 5b, 2, lambda ver.: each second element from a list of numbers
lambda_each_second = lambda alist: [x for x in alist if x % 2 == 0]

# 5c: squares of even elements on uneven positions;
# Is it possible to avoid double "for statement" for this task and write it in one\two lines?
def mixed_second(alist):
    return [x**2 for x in alist if x % 2 == 0 and alist.index(x) % 2 != 0]


print "5a, 1: squaring:", squaring(alist_2)
print "5a, 2: lambda_squaring:", lambda_squaring(alist_2)
print "5b, 1: each_second:", each_second(alist_2)
print "5b, 2: lambda_each_second:", lambda_each_second(alist_2)
# print "mixed:", list(mixed_second(alist_2))
