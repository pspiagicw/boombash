from unittest import TestCase
from boombash import token
from boombash import tokenizer
from boombash import parser
from boombash import token


class TestParser(TestCase):
    def get_tokens(self, token_input):
        tokenizer_instance = tokenizer.Tokenizer(token_input)
        tokens = list()
        while not tokenizer_instance.EOF:
            tokens.append(tokenizer_instance.next_token())
        return tokens

    def test_simple(self):
        input = "( ls )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        ideal_representation = [token.Token(token.IDENT, "ls")]
        self.assertEqual(ideal_representation, parsed_representation)

    def test_simple_nested(self):
        input = "( ( ls ) )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        ideal_representation = [[token.Token(token.IDENT, "ls")]]
        self.assertEqual(ideal_representation, parsed_representation)

    def test_advanced_nested(self):
        input = "( ls ( ls )  ls)"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        ideal_representation = [
            token.Token(token.IDENT, "ls"),
            [
                token.Token(token.IDENT, "ls"),
            ],
            token.Token(token.IDENT, "ls"),
        ]
        self.assertEqual(ideal_representation, parsed_representation)
