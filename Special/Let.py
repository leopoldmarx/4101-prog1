# Let -- Parse tree node strategy for printing the special form let

from Special import Special

class Let(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.
        sys.stdout.write("(")
        t.car.print(n)
        print("\r")
        t.cdr.print(n=4, p=False)
        pass
