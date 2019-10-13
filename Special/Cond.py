# Cond -- Parse tree node strategy for printing the special form cond
import sys

from Special import Special

class Cond(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        sys.stdout.write("cond ")
        t.cdr.print(-abs(n) - 4, p=True)
