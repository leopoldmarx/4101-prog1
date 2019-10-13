# Regular -- Parse tree node strategy for printing regular lists
import sys

from Special import Special

class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        if t.car.isNull():
            sys.stdout.write('(')
        t.car.print(abs(n),p=not t.car.isPair())

        #cdr
        if t.cdr.isPair():
            sys.stdout.write(' ')
            t.cdr.print(n,p=True)
        elif t.cdr.isNull():
            t.cdr.print(n, p=True)
        else:
            sys.stdout.write(' . ')
            t.cdr.print(n, p=True)
            sys.stdout.write(')')