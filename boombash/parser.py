
import sys
from boombash import token


class Parser:
    def __init__(self,tokens):
        self.tokens = tokens

    def parse(self , tokens=None):
        if tokens == None:
            tokens = self.tokens
        representation = list()
        remaining = list()
        index = 0
        if len(tokens) == 0:
            return remaining , representation
        if tokens[0].Type == token.LPAREN:
            index += 1
        while index < len(tokens):
            if tokens[index].Type == token.LPAREN:
                next_remaining , next_representation = self.parse(tokens[index+1:])
                representation.append(next_representation)
                tokens = next_remaining
                index = 0
                continue
            elif tokens[index].Type == token.RPAREN:
                return tokens[index+1:] , representation
            else:
                representation.append(tokens[index])
            index += 1


                

        return remaining , representation


            

