
import subprocess
from boombash import token
class Executor:
    def __init__(self ,variables = dict() ,  functions = dict() , code=None , argument_structure = None):
        self.functions = functions
        self.variables = variables
        self.code = code
        self.argument_structure = argument_structure
    def exec(self,data=None , args = None):
        if data == None:
            data = self.code
        if not isinstance(data,list):
            return data.Literal
        if self.argument_structure:
            print(args)
            assert len(self.argument_structure) == len(args) , "No of arguments differ"
            for i in range(len(args)):
                self.variables[self.argument_structure[i]] = args[i]
        operator = data[0]
        if operator.Type == token.PLUS:
            assert len(data) == 3 , "Add function expects 2 arguments only"
            return int(self.exec(data[1] , args=args)) + int(self.exec(data[2] , args=args))
        if operator.Type == token.MINUS:
            assert len(data) == 3 , "Minus function expects 2 arguments only"
            return int(self.exec(data[1])) - int(self.exec(data[2]))
        if operator.Type == token.MULTIPLY:
            assert len(data) == 3 , "Multiply function expects 2 arguments only"
            return int(self.exec(data[1])) * int(self.exec(data[2]))
        if operator.Type == token.DIVIDE:
            assert len(data) == 3 , "Divide function expects 2 arguments only"
            return int(self.exec(data[1])) / int(self.exec(data[2]))
        if operator.Type == token.MOD:
            assert len(data) == 3 , "Modulus function expects 2 arguments only"
            return int(self.exec(data[1] , args=args)) % int(self.exec(data[2]))
        if operator.Type == token.OUTPUT:
            assert len(data) == 2 , "Type function expects 1 argument"
            print(self.exec(data[1] , args=args))
        if operator.Type == token.EQ:
            assert len(data) == 3 , "Eq function expects 2 arguments"
            return self.exec(data[1]) == self.exec(data[2])
        if operator.Type == token.IF:
            assert len(data) == 4 , "If function expects 3 arguments"
            if self.exec(data[1]) == True:
                self.exec(data[2])
            else:
                self.exec(data[3])
        if operator.Type == token.WHILE:
            assert len(data) == 3 , "While function expects 2 arguments"
            while self.exec(data[1]) == True:
                self.exec(data[2])
        if operator.Type == token.VAR:
            assert len(data) == 3 , "Var function expects 2 arguments"
            self.variables[self.exec(data[1])] = self.exec(data[2])
        if operator.Type == token.GET:
            assert len(data) == 2 , "Get function expects 1 arguments"
            return self.variables[self.exec(data[1])]
        if operator.Type == token.DEFUN:
            assert len(data) == 4 , "Function expects 3 arguments"
            for arg in data[2]:
                assert isinstance(arg , list) == False , "Argument should be only name of variables"
            self.functions[self.exec(data[1])] = Executor(self.variables , self.functions , data[3] , argument_structure=data[2])
        if operator.Type == token.IDENT:
            if self.exec(operator) in self.functions:
                self.functions[self.exec(operator)].exec(args=data[1:])


                
            
            


