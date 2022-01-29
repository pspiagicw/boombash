from unittest import TestCase
from boombash import executor, parser, tokenizer , token


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
        correct_token = token.Token(Type= token.INT , Literal = '7')
        self.assertEqual(output, correct_token)

    def test_simple_minus(self):
        input = "(- 3 4 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token(Type= token.INT , Literal = '-1')
        self.assertEqual(output, correct_token)

    def test_simple_multiply(self):
        input = "(* 3 4 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token(Type= token.INT , Literal = '12')
        self.assertEqual(output, correct_token)

    def test_simple_divide(self):
        input = "(/ 12 3 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token(Type = token.INT , Literal = '4')
        self.assertEqual(output, correct_token)

    def test_simple_mod(self):
        input = "(% 3 2 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token(Type = token.INT , Literal = '1')
        self.assertEqual(output, correct_token)

    def test_simple_eq(self):
        input = "(= 3 2 )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token._make_false_token()
        self.assertEqual(output, correct_token)

    def test_intermediate_eq(self):
        input = "(= 3 (+ 1 2))"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token._make_true_token()
        self.assertEqual(output, correct_token)

    def test_intermediate_eq2(self):
        input = "(= 3 (- 4 1))"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token._make_true_token()
        self.assertEqual(output, correct_token)

    def test_intermediate_eq3(self):
        input = "(= 'Hello' 3)"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token._make_false_token()
        self.assertEqual(output, correct_token)

    def test_intermediate_eq4(self):
        input = "(= 'Hello' 'Hello')"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token._make_true_token()
        self.assertEqual(output, correct_token)

    def test_intermediate_eq5(self):
        input = "(= 'Hello World' (+ 'Hello ' 'World'))"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tokens = self.get_tokens(input)[:-1]
        # token_str = list(map(str,get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor()
        output = executor_instance.exec(parsed_representation)
        correct_token = token.Token._make_true_token()
        self.assertEqual(output, correct_token)

