from boombash import token


class Tokenizer:
    """This class gives token depending on input"""
    def __init__(self, input):
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
        char = None
        if not self.EOF:
            char = self.input[self.current_position]
        while (not self.EOF) and (
            char
            in [
                "\n",
                "\t ",
                " ",
                "\r",
            ]
        ):
            self.move_position()
            if not self.EOF:
                char = self.input[self.current_position]

    def next_token(self):
        self.move_position()
        self.eat_space()
        if self.EOF:
            return token.Token(Type=token.EOF, Literal="EOF")
        char = self.input[self.current_position]
        token_instance = None
        if char == "(":
            token_instance = token.Token(Type=token.LPAREN, Literal=char)
        elif char == ")":
            token_instance = token.Token(Type=token.RPAREN, Literal=char)
        elif char == "+":
            token_instance = token.Token(Type=token.PLUS, Literal=char)
        elif char == "-":
            token_instance = token.Token(Type=token.MINUS, Literal=char)
        elif char == "$":
            ident = self.read_variable()
            token_instance = token.Token(Type=token.RETRIEVE, Literal=ident[1:])
        elif char.isalpha():
            ident = self.read_identifier()
            if ident == token.PRINT:
                token_instance = token.Token(Type=token.PRINT, Literal=ident)
            elif ident == token.IF:
                token_instance = token.Token(Type=token.IF, Literal=ident)
            elif ident == token.WHILE:
                token_instance = token.Token(Type=token.WHILE, Literal=ident)
            elif ident == token.VAR:
                token_instance = token.Token(Type=token.VAR, Literal=ident)
            elif ident == token.GET:
                token_instance = token.Token(Type=token.GET, Literal=ident)
            elif ident == token.DEFUN:
                token_instance = token.Token(Type=token.DEFUN, Literal=ident)
            elif ident == token.EX:
                token_instance = token.Token(Type=token.EX, Literal=ident)
            elif ident == token.LT:
                token_instance = token.Token(Type=token.LT, Literal=ident)
            elif ident == token.GT:
                token_instance = token.Token(Type=token.GT, Literal=ident)
            elif ident == token.LE:
                token_instance = token.Token(Type=token.LE, Literal=ident)
            elif ident == token.GE:
                token_instance = token.Token(Type=token.GE, Literal=ident)
            else:
                token_instance = token.Token(Type=token.IDENT, Literal=ident)
        elif char.isnumeric():
            numerical = self.read_number()
            token_instance = token.Token(Type=token.INT, Literal=numerical)
        elif char == "/":
            token_instance = token.Token(Type=token.DIVIDE, Literal=char)
        elif char == "*":
            token_instance = token.Token(Type=token.MULTIPLY, Literal=char)
        elif char == "'":
            string = self.read_string()
            token_instance = token.Token(Type=token.STRING, Literal=string)
        elif char == "=":
            token_instance = token.Token(Type=token.EQ, Literal=char)
        elif char == "%":
            token_instance = token.Token(Type=token.MOD, Literal=char)
        return token_instance

    def read_string(self):
        oldposition = self.read_position
        char = self.input[self.read_position]
        while char != "'" and self.read_position < len(self.input):
            self.move_position()
            char = self.input[self.current_position]
        string = self.input[oldposition : self.read_position - 1]
        return string

    def read_identifier(self):
        oldposition = self.current_position
        char = self.input[self.current_position]
        while char.isalpha() and self.read_position < len(self.input):
            if self.input[self.read_position].isalpha():
                self.move_position()
            else:
                break
            char = self.input[self.current_position]
        ident = self.input[oldposition : self.read_position]
        return ident

    def read_variable(self):
        oldposition = self.current_position
        char = self.input[self.current_position]
        while (char.isalpha() or char == "$") and self.read_position < len(self.input):
            if self.input[self.read_position].isalpha():
                self.move_position()
            else:
                break
            char = self.input[self.current_position]
        ident = self.input[oldposition : self.read_position]
        return ident

    def read_number(self):
        oldposition = self.current_position
        char = self.input[self.current_position]
        while char.isnumeric() and self.read_position < len(self.input):
            if self.input[self.read_position].isnumeric():
                self.move_position()
            else:
                break
            char = self.input[self.current_position]
        number = self.input[oldposition : self.read_position]
        return number
