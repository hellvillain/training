alist_1 = range(1, 20)
alist_2 = range(0, 20)


# 5a, 1, def ver.: making squares from a list of numbers
def squaring(alist):
    return [x**2 for x in alist]

# 5a, 2, lambda ver.:  making squares from a list of numbers
lambda_squaring = lambda alist: [x**2 for x in alist]


# 5b, 1, def ver.: each second element from a list of numbers
def each_second(alist):
    return [x for x in alist if x % 2 == 0]


# 5b, 1, def ver.: right version with slice
def each_second_slice(alist):
    return alist[0::2]


# 5b, 2, lambda ver.: each second element from a list of numbers
lambda_each_second = lambda alist: [x for x in alist if x % 2 == 0]


# 5c: each_second_mixed starting with zero, slice version 
def each_second_mixed_slice(alist):
    return [x*x for x in alist if x % 2 == 0][1::2]


print "5a, 1: squaring:", squaring(alist_2)
print "5a, 2: lambda_squaring:", lambda_squaring(alist_2)
print "5b, 1: each_second, bycicle type:", each_second(alist_2)
print "5b, 1: each_second with slices:", each_second_slice(alist_2)
print "5b, 2: lambda_each_second:", lambda_each_second(alist_2)
print "5c: mixed with slices:", each_second_mixed_slice(alist_2)
