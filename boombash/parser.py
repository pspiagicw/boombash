from boombash import token


class Parser:
    """Takes a stream/list of tokens and converts into a tree-representation """
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self, tokens=None):
        """Parses the tokens given

        Signature:
        parse(tokens) --> remaining , representation
        Arguments:
        tokens: List of tokens encountered (Most of the time comes from the Parser class)

        Returns:
        representation: Tree structure as a list-of-lists
        remaining: Tokens that have to be still parsed.(if parsed correctly this will be empty)
        """
        if tokens == None:
            tokens = self.tokens
        representation = list()
        remaining = list()
        index = 0
        if len(tokens) == 0:
            return remaining, representation
        if tokens[0].Type == token.LPAREN:
            index += 1
        while index < len(tokens):
            if tokens[index].Type == token.LPAREN:
                next_remaining, next_representation = self.parse(tokens[index + 1 :])
                representation.append(next_representation)
                tokens = next_remaining
                index = 0
                continue
            elif tokens[index].Type == token.RPAREN:
                return tokens[index + 1 :], representation
            else:
                representation.append(tokens[index])
            index += 1

        return remaining, representation
