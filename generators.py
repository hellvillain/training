alist_1 = range(1, 20, 1)
alist_2 = range(1, 20, 1)

#4 a ii: own xrange generator
class Xray(object):

    def __init__(self, start, stop=None, step=1):
        self._start, self._stop, self._step = start, stop, step

    def __iter__(self):
        number = self._start
        while cmp(number, self._stop) == cmp(0, self._step):
            yield number
            number += self._step

# 4b: own zip perfomance
def zipping(alist_1, alist_2):
    if len(alist_1) != len(alist_2):
        print "You brought up lists with wrong length"
        return None
    else:
        zipped = ((x,y) for x in alist_1 for y in alist_2 if alist_1.index(x) == alist_2.index(y))
        return list(zipped)

print "4a ii, xrange perfomance:", list(Xray(0, 9, 2))
print "4b, original zip output:", zip(alist_1, alist_2)
print "4b, my zip output:", zipping(alist_1, alist_2)
