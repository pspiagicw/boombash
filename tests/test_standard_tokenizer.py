from unittest import TestCase

from boombash import token
from boombash import tokenizer


class TestStandardTokenizer(TestCase):
    def test_standard_token_1(self):
        input = "( defun )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.DEFUN, Literal="defun"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_2(self):
        input = "( + )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.PLUS, Literal="+"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_3(self):
        input = "( - )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MINUS, Literal="-"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_4(self):
        input = "( * )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MULTIPLY, Literal="*"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_5(self):
        input = "( / )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.DIVIDE, Literal="/"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_6(self):
        input = "( % )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MOD, Literal="%"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_7(self):
        input = "( = )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.EQ, Literal="="),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_8(self):
        input = "( hello )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.IDENT, Literal="hello"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_9(self):
        input = "( 10 )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.INT, Literal="10"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_10(self):
        input = "( 'something' )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.STRING, Literal="something"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_11(self):
        input = "( if )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.IF, Literal="if"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_12(self):
        input = "( while )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.WHILE, Literal="while"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_13(self):
        input = "( get )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.GET, Literal="get"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_14(self):
        input = "( ex )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.EX, Literal="ex"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_standard_token_15(self):
        input = "( output )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.OUTPUT, Literal="output"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)
