# Let -- Parse tree node strategy for printing the special form let
import sys

from Special import Special

class Let(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        sys.stdout.write("let ")
        t.cdr.car.print(n, p=not t.cdr.car.isPair())
        t.cdr.cdr.print(-abs(n) - 4, p=True)
