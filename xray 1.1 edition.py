class Xray(object):

    def __init__(self, start, stop=None, step=1):
        self._start, self._stop, self._step = start, stop, step

    def __iter__(self):
        number = self._start
        while cmp(number, self._stop) == cmp(0, self._step):
            yield number
            number += self._step

my_list = Xray(0, 9, 3)
print list(my_list)