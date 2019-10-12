# Regular -- Parse tree node strategy for printing regular lists
import sys

from Special import Special

class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        if p:
            t.car.print(n, p=False)
        else:
            sys.stdout.write('(')
            t.car.print(n,p=True)
