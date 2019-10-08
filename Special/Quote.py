# Quote -- Parse tree node strategy for printing the special form quote
import sys

from Special import Special

class Quote(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        sys.stdout.write("'")
        #t..print(n, p)
        t.cdr.car.print(n)
        pass
