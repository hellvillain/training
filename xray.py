class Xray(object):

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.index = start

    def __iter__(self):
        return self

    def next(self):
        if self.index == self.start and self.start + self.step < self.stop:
            self.index = self.stop
            return self.start
        while self.start + self.step < self.stop:
            self.start += self.step
            return self.start

        raise StopIteration

my_list = Xray(0, 9, 2)
print list(my_list)

