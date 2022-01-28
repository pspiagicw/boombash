import unittest
from boombash import token

class TestTokenClass(unittest.TestCase):
    def test_simple(self):
        token1 = token.Token(Type=token.WHILE, Literal = 'while' )
        token2 = token.Token(Type=token.IDENT ,Literal =  'while' )


        token_false = token.Token(token.FALSE , 'false')
        self.assertEqual(token1 == token2 , token_false)


    def test_number(self):
        token1 = token.Token(Type=token.INT , Literal = '5')
        token2 = token.Token(Type=token.INT, Literal = '7')

        token_false = token.Token(token.FALSE , 'false')
        self.assertEqual(token1 == token2 , token_false )

    def test_comparison(self):
        token1 = token.Token(token.INT,'5')
        token2 = token.Token(token.INT , '7')

        token_true = token.Token(token.TRUE , 'true')
        token_false = token.Token(token.FALSE , 'false')
        self.assertEqual(token1 < token2 , token_true)
        self.assertEqual(token1 > token2, token_false)
        self.assertEqual(token1 <= token2 , token_true)
        self.assertEqual(token1 >= token2 , token_false)

    def test_string_add(self):
        token1 = token.Token(token.STRING , 'hello ')
        token2 = token.Token(token.STRING , 'world ')

        token3 = token.Token(token.STRING , 'hello world')
        self.assertEqual(token1 + token2 , token3 )

    def test_number_add(self):
        token1 = token.Token(token.INT , '5')
        token2 = token.Token(token.INT , '7')

        token3 = token.Token(token.INT , '12')
        self.assertEqual(token1 + token2 , token3 )
    def test_number_substract(self):
        token1 = token.Token(token.INT , '5')
        token2 = token.Token(token.INT , '7')

        token4 = token.Token(token.INT , '-2')
        self.assertEqual(token1 - token2 , token4 )
    def test_number_multiply(self):
        token1 = token.Token(token.INT , '5')
        token2 = token.Token(token.INT , '7')

        token5 = token.Token(token.INT , '35')
        self.assertEqual(token1 * token2 , token5 )

    def test_number_divide(self):
        token1 = token.Token(token.INT , '5')
        token2 = token.Token(token.INT , '5')
        token6 = token.Token(token.INT , '1')

        self.assertEqual(token1 / token2 , token6 )

    def test_token_mod(self):
        token1 = token.Token(token.INT , '5 ')
        token2 = token.Token(token.INT , '2')

        token7 = token.Token(token.INT , '1')
        self.assertEqual(token1 % token2 , token7 )

    def test_token_abs(self):
        token1 = token.Token(token.INT , '-7')

        token2 = token.Token(token.INT , '7')
        self.assertEqual(abs(token1) , token2 )

    # def test_token_bool(self):
    #     token1 = token.Token(token.INT , '5')
    #     token2 = token.Token(token.INT , '0 ')
    #     token3 = token.Token(token.STRING , '')
    #     token4 = token.Token(token.STRING , 'hello')

    #     token_true = token.Token(token.TRUE  , 'true')
    #     token_false = token.Token(token.FALSE  , 'false')

    #     self.assertEqual(bool(token1) , token_true )
    #     self.assertEqual(bool(token2) , token_false )
    #     self.assertEqual(bool(token3) , token_false)
    #     self.assertEqual(bool(token4) , token_true)


