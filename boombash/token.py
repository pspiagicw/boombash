DEFUN = 'defun'
LPAREN = '('
RPAREN = ')'

PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'
MOD = '%'
EQ = '='

IDENT = 'IDENT'
INT = 'INT'
STRING = 'STRING'
LIST = 'LIST'
IF = 'if'
WHILE = 'while'
OUTPUT = 'output'
VAR = 'var'
GET = 'get'


EOF = 'EOF'

class Token:
    """The Token Class , contains framwork for creating more tokens"""
    def __init__(self,Type , Literal):
        self.Type = Type
        self.Literal = Literal
    def __str__(self):
        return "Token[ Type =  '{type}' , Literal= '{literal}' ]".format(type=self.Type , literal = self.Literal)
    def __repr__(self):
        return "Token[ Type =  '{type}' , Literal= '{literal}' ]".format(type=self.Type , literal = self.Literal)
    



