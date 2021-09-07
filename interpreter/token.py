
FUNC = 'FUNC'
LPAREN = '('
RPAREN = ')'

PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'
MOD = '%'

IDENT = 'IDENT'
INT = 'INT'
STRING = 'STRING'
LIST = 'LIST'
IF = 'IF'


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
    

class Tokenizer:
    """This class gives token depending on input"""
    def __init__(self,input):
        self.input = input
        self.current_position = -1
        self.read_position = 0
        self.EOF = False
    def move_position(self):
        self.current_position = self.read_position
        self.read_position += 1
        if self.current_position == len(self.input):
            self.EOF = True
    def eat_space(self):
        char = self.input[self.current_position]
        if char in [ '\n' , '\t ' , ' ' , '\r' ]:
            self.move_position()
    def next_token(self):
        self.move_position()
        if self.EOF:
            return Token(Type = EOF , Literal = 'EOF')
        self.eat_space()
        char = self.input[self.current_position]
        token = None

        if char == '(':
            token = Token(Type = LPAREN , Literal = char)
        elif char == ')':
            token = Token(Type = RPAREN , Literal = char)
        elif char == '+':
            token = Token(Type = PLUS , Literal = char)
        elif char == '-':
            token = Token(Type = MINUS , Literal = char)
        elif char.isalpha():
            ident = self.read_identifier()
            token = Token(Type = IDENT , Literal = ident)
        elif char.isnumeric():
            numerical = self.read_number()
            token = Token(Type = INT , Literal = numerical)
        elif char == '/':
            token = Token(Type = DIVIDE , Literal = char)
        elif char == '*':
            token = Token(Type = MULTIPLY , Literal = char)
        return token
    def read_identifier(self):
        oldposition = self.current_position
        char = self.input[self.current_position]
        while char.isalpha() and self.read_position < len(self.input):
            self.move_position()
            char = self.input[self.current_position]
        ident = self.input[oldposition:self.read_position]
        return ident
            
    def read_number(self):
        oldposition = self.current_position
        char = self.input[self.current_position]
        while char.isnumeric() and self.read_position < len(self.input):
            self.move_position()
            char = self.input[self.current_position]
        number = self.input[oldposition:self.read_position]
        return number


