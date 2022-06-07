import time

class Recession:

    def __init__(self, start:time, end:time) -> None:
        self.start = start
        self.end = end

    def last(self):
        return self.end - self.start
