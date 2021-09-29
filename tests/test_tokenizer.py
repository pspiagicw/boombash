from unittest import TestCase

from boombash import token, tokenizer


class TestTokenizer(TestCase):
    def test_parens(self):
        input = "()()(("
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_strings(self):
        input = "  'hello'"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.STRING, Literal="hello"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_strings_func(self):
        input = "(+ 'hello' )"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.PLUS, Literal="+"),
            token.Token(Type=token.STRING, Literal="hello"),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_parens_tricky(self):
        input = "()()  (("
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_plus(self):
        input = "(+()(+"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.PLUS, Literal="+"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.PLUS, Literal="+"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_plus_tricky(self):
        input = "(+ (  )(+"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.PLUS, Literal="+"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.PLUS, Literal="+"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_minus(self):
        input = "(-()(-"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MINUS, Literal="-"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MINUS, Literal="-"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_minus_tricky(self):
        input = "  (-()  (-"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MINUS, Literal="-"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MINUS, Literal="-"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_multiply(self):
        input = "(*()(*"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MULTIPLY, Literal="*"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MULTIPLY, Literal="*"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_multiply_tricky(self):
        input = "(   *()(     *"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MULTIPLY, Literal="*"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.MULTIPLY, Literal="*"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_divide(self):
        input = "(/()(/"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.DIVIDE, Literal="/"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.DIVIDE, Literal="/"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_divide_tricky(self):
        input = "(/    ( )(/"
        tokenizer_instance = tokenizer.Tokenizer(input)
        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.DIVIDE, Literal="/"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.RPAREN, Literal=")"),
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.DIVIDE, Literal="/"),
            token.Token(Type=token.EOF, Literal="EOF"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_ident(self):
        input = "( ident"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.IDENT, Literal="ident"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_integer(self):
        input = "( 55"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.INT, Literal="55"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_integer_tricky(self):
        input = "( 55  )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.INT, Literal="55"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_indent_tricky(self):
        input = "(ident)"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.IDENT, Literal="ident"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_indent_tricky2(self):
        input = "(  ident  )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.IDENT, Literal="ident"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)

    def test_indent_tricky3(self):
        input = "(     ident  )"
        tokenizer_instance = tokenizer.Tokenizer(input)

        tests = [
            token.Token(Type=token.LPAREN, Literal="("),
            token.Token(Type=token.IDENT, Literal="ident"),
            token.Token(Type=token.RPAREN, Literal=")"),
        ]
        for i in range(len(tests)):
            given_token = tokenizer_instance.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type, ideal_token.Type)
            self.assertEqual(given_token.Literal, ideal_token.Literal)
