# Scanner -- The lexical analyzer for the Scheme printer and interpreter

import sys
import io
from Tokens import *
import string

class Scanner:
    def __init__(self, i):
        self.In = i
        self.buf = []
        self.ch_buf = None

    def read(self):
        if self.ch_buf == None:
            return self.In.read(1)
        else:
            ch = self.ch_buf
            self.ch_buf = None
            return ch
    
    def peek(self):
        if self.ch_buf == None:
            self.ch_buf = self.In.read(1)
            return self.ch_buf
        else:
            return self.ch_buf

    @staticmethod
    def isDigit(ch):
        return ch >= '0' and ch <= '9'

    @staticmethod
    def isInitial(ch):
        return (ch >= 'a' and ch <= 'z') or ch == '!' or ch == '$' or ch == '%' or ch == '&' or ch == '*' or ch == '/' or ch == ':' or ch == '<' or ch == '=' or ch == '>' or ch == '?' or ch == '^' or ch == '_' or ch == '~'

    @staticmethod
    def isPeculiar(ch):
        return ch=='+' or ch=='-'

    @staticmethod
    def isSubsequent(ch):
        return Scanner.isInitial(ch) or Scanner.isDigit(ch) or Scanner.isSpecialSubsequent(ch)

    @staticmethod
    def isSpecialSubsequent(ch):
        return ch == '+' or ch == '-' or ch == '.' or ch == '@'

    def getNextToken(self):
        try:
            # It would be more efficient if we'd maintain our own
            # input buffer for a line and read characters out of that
            # buffer, but reading individual characters from the
            # input stream is easier.
            ch = self.read()

            # TODONE: Skip white space and comments

            #simple whileloop to remove whitespace. \r is whitespace and \n determines the end of the line

            # whitespace
            if ch in string.whitespace:
                ch = self.read()
                while ch in string.whitespace:
                    ch = self.read()

            #comments
            if ch == ';':
                ch= self.read()
                while ch != '\n':
                    ch = self.read()
            # if ch == '\n':
            #     ch = self.read()

            # Return None on EOF
            if ch == "":
                return None
    
            # Special characters
            elif ch == '\'':
                return Token(TokenType.QUOTE)
            elif ch == '(':
                return Token(TokenType.LPAREN)
            elif ch == ')':
                return Token(TokenType.RPAREN)
            elif ch == '.':
                #  We ignore the special identifier `...'.
                return Token(TokenType.DOT)

            # Boolean constants
            elif ch == '#':
                ch = self.read()

                if ch == 't':
                    return Token(TokenType.TRUE)
                elif ch == 'f':
                    return Token(TokenType.FALSE)
                elif ch == "":
                    sys.stderr.write("Unexpected EOF following #\n")
                    return None
                else:
                    sys.stderr.write("Illegal character '" +
                                     chr(ch) + "' following #\n")
                    return self.getNextToken()

            # String constants
            elif ch == '"':
                self.buf = []
                ch = self.read()
                while ch != '"':
                    self.buf.append(ch)
                    ch = self.read()
                # TODONE: scan a string into the buffer variable buf
    
                return StrToken("".join(self.buf))

            # Integer constants
            elif self.isDigit(ch):
                i = ord(ch) - ord('0')
                # TODONE: scan the number and convert it to an integer
                while self.isDigit(self.peek()):
                    i = i*10 + ord(self.read()) - ord('0')
                # make sure that the character following the integer
                # is not removed from the input stream
                return IntToken(i)
    
            # Identifiers
            elif self.isInitial(ch):
                # or ch is some other vaid first character
                # for an identifier
                self.buf = []
                # TODO: scan an identifier into the buffer variable buf
                self.buf.append(ch)

                while self.isSubsequent(self.peek()):
                    self.buf.append(self.read())

                # make sure that the character following the identifier
                # is not removed from the input stream
                return IdentToken("".join(self.buf))

            elif self.isPeculiar(ch):
                return IdentToken(ch)


            # Illegal character
            else:
                sys.stderr.write("Illegal input character '" + ch + "'\n")
                return self.getNextToken()

        except IOError:
            sys.stderr.write("IOError: error reading input file\n")
            return None


if __name__ == "__main__":
    scanner = Scanner(sys.stdin)
    tok = scanner.getNextToken()
    tt = tok.getType()
    print(tt)
    if tt == TokenType.INT:
        print(tok.getIntVal())
