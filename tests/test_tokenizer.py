
from unittest import TestCase
from interpreter import token


class TestTokenizer(TestCase):
    def test_parens(self):
        input = "()()(("
        tokenizer = token.Tokenizer(input)
        tests = [
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.RPAREN , Literal = ')'),
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.RPAREN , Literal = ')'),
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.EOF , Literal = 'EOF'),
        ]
        for i in range(len(tests)):
            given_token = tokenizer.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type , ideal_token.Type)
            self.assertEqual(given_token.Literal , ideal_token.Literal)

    def test_plus(self):
        input = "(+()(+"
        tokenizer = token.Tokenizer(input)
        tests = [
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.PLUS , Literal = '+'),
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.RPAREN , Literal = ')'),
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.PLUS , Literal = '+'),
            token.Token(Type = token.EOF , Literal = 'EOF'),
        ]
        for i in range(len(tests)):
            given_token = tokenizer.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type , ideal_token.Type)
            self.assertEqual(given_token.Literal , ideal_token.Literal)
            
    def test_minus(self):
        input = "(-()(-"
        tokenizer = token.Tokenizer(input)
        tests = [
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.MINUS , Literal = '-'),
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.RPAREN , Literal = ')'),
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.MINUS , Literal = '-'),
            token.Token(Type = token.EOF , Literal = 'EOF'),
        ]
        for i in range(len(tests)):
            given_token = tokenizer.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type , ideal_token.Type)
            self.assertEqual(given_token.Literal , ideal_token.Literal)
    def test_ident(self):
        input = "( ident"
        tokenizer = token.Tokenizer(input)
        
        tests = [
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.IDENT , Literal = 'ident')
        ]
        for i in range(len(tests)):
            given_token = tokenizer.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type , ideal_token.Type)
            self.assertEqual(given_token.Literal , ideal_token.Literal)

    def test_integer(self):
        input = "( 55"
        tokenizer = token.Tokenizer(input)
        
        tests = [
            token.Token(Type = token.LPAREN , Literal = '('),
            token.Token(Type = token.INT , Literal = '55')
        ]
        for i in range(len(tests)):
            given_token = tokenizer.next_token()
            ideal_token = tests[i]
            self.assertEqual(given_token.Type , ideal_token.Type)
            self.assertEqual(given_token.Literal , ideal_token.Literal)
