from unittest import TestCase

from boombash import executor
from boombash import parser
from boombash import tokenizer


class TestExecutor(TestCase):
    def get_tokens(self, token_input):
        tokenizer_instance = tokenizer.Tokenizer(token_input)
        tokens = list()
        while not tokenizer_instance.EOF:
            tokens.append(tokenizer_instance.next_token())
        return tokens

    def test_simple_add(self):
        input = "(+ 3 4 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        self.assertEqual(output, 7)

    def test_simple_minus(self):
        input = "(- 3 4 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        self.assertEqual(output, -1)

    def test_simple_multiply(self):
        input = "(* 3 4 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        self.assertEqual(output, 12)

    def test_simple_divide(self):
        input = "(/ 12 3 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        self.assertEqual(output, 4)

    def test_simple_mod(self):
        input = "(% 3 2 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        self.assertEqual(output, 1)
