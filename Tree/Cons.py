# Cons -- Parse tree node class for representing a Cons node
from Special import *
from Tree import Node
from Tree import Ident

class Cons(Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.
    def parseList(self):
        # TODO: implement this function and any helper functions
        if self.car.isSymbol():

            name = self.car.name.lower()
            if name=="quote" or "'":
                self.car = Quote()
                print(name)

            elif name=="lambda":
                self.car = Lambda()

            elif name=="begin":
                self.car = Begin()

            elif name=="if":
                self.car = If()

            elif name=="let":
                self.car = Let()

            elif name=="cond":
                self.car = Cond()

            elif name=="define":
                self.car = Define()

            elif name=="set":
                self.car = Set()

            elif name=="regular":
                self.car = Regular()

        # you might need
        self.form = None

    def print(self, n, p=False):
        #self.form.print(self, n, p)
        print(self.car)
        if self.car.isPair():
            self.car.print(n+1)
        else:
            print(self.car)
        if self.cdr.isPair():
            self.cdr.print(n+1)
        else:
            print(self.cdr)

    def isPair(self):
        return True

    def getCar(self):
        return self.car

    def getCdr(self):
        return self.cdr

    def setCar(self, a):
        self.car = a
        self.parseList()

    def setCdr(self, d):
        self.cdr = d

if __name__ == "__main__":
    c = Cons(Ident("Hello"), Ident("World"))
    c.print(0)
