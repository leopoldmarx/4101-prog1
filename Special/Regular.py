# Regular -- Parse tree node strategy for printing regular lists

from Special import Special

class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        t.car.print(n,p)
        t.cdr.print(n,p)
