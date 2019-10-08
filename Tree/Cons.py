# Cons -- Parse tree node class for representing a Cons node
import sys

from Special import *
from Tree import *

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
                self.form = 'quote'
                self.car = Quote()

            elif name=="lambda":
                self.form = name
                self.car = Lambda()

            elif name=="begin":
                self.form = name
                self.car = Begin()

            elif name=="if":
                self.form = name
                self.car = If()

            elif name=="let":
                self.form = name
                self.car = Let()

            elif name=="cond":
                self.form = name
                self.car = Cond()

            elif name=="define":
                self.form = name
                self.car = Define()

            elif name=="set" or name=="set!":
                self.form = name
                self.car = Set()

            else:
                self.form = None

        # you might need
        self.form = None

    def print(self, n, p=False):
        # TODO print stuff (this is probably wrong)
        if self.form is None:
            #regular print
            self.car.print(n)
            self.cdr.print(n)
        elif self.form is 'quote':
            self.form.print(self.cdr.car,n)
            self.form.print(self, n, p)

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
