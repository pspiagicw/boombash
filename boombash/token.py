DEFUN = "defun"
LPAREN = "("
RPAREN = ")"

PLUS = "+"
MINUS = "-"
MULTIPLY = "*"
DIVIDE = "/"
MOD = "%"

EQ = "eq"
LT = 'lt'
LE = 'le'
GE = 'ge'
GT = 'gt'


IDENT = "IDENT"
INT = "INT"
STRING = "STRING"
LIST = "LIST"
IF = "if"
WHILE = "while"
EX = "ex"
PRINT = "print"
VAR = "var"
GET = "get"
RETRIEVE = "RETREIVE"

EOF = "EOF"


class Token:
    """The Token Class , contains framwork for creating more tokens"""

    def __init__(self, Type, Literal):
        self.Type = Type
        self.Literal = Literal

    def __str__(self):
        return "Token[ Type =  '{type}' , Literal= '{literal}' ]".format(
            type=self.Type, literal=self.Literal
        )

    def __repr__(self):
        return "Token[ Type =  '{type}' , Literal= '{literal}' ]".format(
            type=self.Type, literal=self.Literal
        )

    def __eq__(self, other):
        if isinstance(other, Token):
            if self.Type == other.Type and self.Literal == other.Literal:
                return True
        if self.Literal == other:
            return True
        return False
