
import subprocess
from interpreter import token
class Executor:
    def exec(self,data):
        if not isinstance(data,list):
            return data.Literal
        else:
            operator = data[0]
            if operator.Type == token.PLUS:
                assert len(data) == 3 , "Add function expects 2 arguments only"
                return float(self.exec(data[1])) + float(self.exec(data[2]))
            if operator.Type == token.MINUS:
                assert len(data) == 3 , "Minus function expects 2 arguments only"
                return float(self.exec(data[1])) - float(self.exec(data[2]))
            if operator.Type == token.MULTIPLY:
                assert len(data) == 3 , "Multiply function expects 2 arguments only"
                return float(self.exec(data[1])) * float(self.exec(data[2]))
            if operator.Type == token.DIVIDE:
                assert len(data) == 3 , "Divide function expects 2 arguments only"
                return float(self.exec(data[1])) / float(self.exec(data[2]))
            if operator.Type == token.MOD:
                assert len(data) == 3 , "Modulus function expects 2 arguments only"
                return float(self.exec(data[1])) % float(self.exec(data[2]))

                
            
            

