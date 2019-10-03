# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys
from Tokens import TokenType
from Tree import *


class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        # TODO: write code for parsing an exp

        tok = self.scanner.getNextToken()
        if tok is None:
            #TODO handle none
            #return None?
            pass

        elif tok is TokenType.LPAREN:
            #TODO ( rest
            #return self.parseRest()?
            pass

        elif tok is TokenType.TRUE:
            return Cons(BoolLit.getInstance(True), self.parseExp())

        elif tok is TokenType.FALSE:
            return Cons(BoolLit.getInstance(False), self.parseExp())

        elif tok is TokenType.QUOTE:
            #TODO ' exp
            pass

        elif tok is TokenType.INT:
            return Cons(IntLit(tok.getIntVal()), self.parseExp())

        elif tok is TokenType.STR:
            return Cons(StrLit(tok.getStrVal()), self.parseExp())

        elif tok is TokenType.IDENT:
            return Cons(Ident(tok.getName()), self.parseExp())

        return None

    def parseRest(self):
        # TODO: write code for parsing a rest

        tok = self.scanner.getNextToken()
        if tok is None:
            #TODO handle none
            #return None?
            pass

        elif tok is TokenType.RPAREN:
            #TODO )
            pass

        else:
            t = self.parseExp()
            return Cons(t, self.parseCont())

        return None

    def parseCont(self):

        tok = self.scanner.getNextToken()
        if tok is None:
            # TODO handle none
            # return None?
            pass

        elif tok is TokenType.DOT:
            #TODO .exp)
            pass

        elif tok is TokenType.RPAREN:
            #TODO )
            pass

        else:
            t = self.parseExp()
            return Cons(t, self.parseCont())

        return None

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
