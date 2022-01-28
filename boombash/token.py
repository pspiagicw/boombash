# This file contains the various tokens used throughout boombash

# Token for Left and Right Parenthesis
LPAREN = "("
RPAREN = ")"

# Symbols
PLUS = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"
MOD = "%"

# These are tokens for some inbuilt functions
EQ = "eq"
LT = "lt"
LE = "le"
GE = "ge"
GT = "gt"


# These are meta tokens , they signify something to the parser and executor , but not to the tokenizer
IDENT = "IDENT"
INT = "INT"
STRING = "STRING"
LIST = "LIST"
RETRIEVE = "RETREIVE"

TRUE = "true"
FALSE = "false"


# These are part of the language itself.
IF = "if"
WHILE = "while"
EX = "ex"
PRINT = "print"
VAR = "var"
GET = "get"
DEFUN = "defun"

EOF = "EOF"


# The
class Token:
    """The Token Class , contains framwork for creating more tokens"""

    def __init__(self, Type, Literal):
        "Every Token contains a Type and a Literal"
        self.Type = Type
        self.Literal = Literal

    def __repr__(self):
        return "Token[ Type =  '{type}' , Literal= '{literal}' ]".format(
            type=self.Type, literal=self.Literal
        )
    @staticmethod
    def _make_true_token():
        "Internal function for making true tokens"
        return Token(TRUE,'true')
    @staticmethod
    def _make_false_token():
        "Internal function for making false tokens"
        return Token(FALSE,'false')

    def __eq__(self, other):
        "True only if both Type and Literal matches"
        if self.Type == other.Type and self.Literal == other.Literal:
            return self._make_true_token()
        return self._make_false_token()

    def __lt__(self , other):
        "Only applies if token is INT"
        if other.Type == self.Type == INT:
            if int(self.Literal) < int(other.Literal):
                return self._make_true_token()
        return self._make_false_token()
    def __le__(self , other):
        "Only applies if token is INT"
        if other.Type == self.Type == INT:
            if int(self.Literal) <= int(other.Literal):
                return self._make_true_token()
        return self._make_false_token()
    def __gt__(self , other):
        "Only applies if token is INT"
        if other.Type == self.Type == INT:
            if int(self.Literal) > int(other.Literal):
                return self._make_true_token()
        return self._make_false_token()

    def __ge__(self , other):
        "Only applies if token is INT"
        if other.Type == self.Type == INT:
            if int(self.Literal) >= int(other.Literal):
                return self._make_true_token()
        return self._make_false_token()
    def __add__(self,other):
        "Adds the two tokens, only if integer"
        if other.Type == self.Type == INT:
            return Token(
                Type = INT,
                Literal = int(other.Literal) + int(self.Literal)
            )
        if other.Type == self.Type == STRING:
            return Token(
                Type = STRING,
                Literal = other.Literal + self.Literal
            )
    def __sub__(self,other):
        "Multiplies the two tokens, only if integer"
        if other.Type == self.Type == INT:
            return Token(
                Type = INT,
                Literal = int(other.Literal) - int(self.Literal)
            )
    def __truediv__(self,other):
        "Divides the two tokens, only if integer"
        if other.Type == self.Type == INT:
            return Token(
                Type = INT,
                Literal = int(other.Literal) / int(self.Literal)
            )
    def __mul__(self,other):
        "Multiplies the two tokens, only if integer"
        if other.Type == self.Type == INT:
            return Token(
                Type = INT,
                Literal = int(other.Literal) * int(self.Literal)
            )
    def __mod__(self,other):
        "Modulo the two tokens, only if integer"
        if other.Type == self.Type == INT:
            return Token(
                Type = INT,
                Literal = int(other.Literal) % int(self.Literal)
            )
    def __abs__(self):
        "Provide absolute values of token"
        if self.Type == INT:
            return Token(
                Type = INT,
                Literal = str(abs(int(self.Literal)))
            )
    def __nonzero__(self):
        "Checks if token is TRUE or FALSE"
        if self.Type == FALSE:
            return False
        if self.Type == INT and self.Literal == '0':
            return False
        if self.Type == STRING and self.Literal == '':
            return False
        return True
        # if self.Type != :
        #     return self._make_true_token()
        # return self._make_false_token()


