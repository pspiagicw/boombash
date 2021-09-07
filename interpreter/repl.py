
import pprint
from interpreter import token
from interpreter import parser
from interpreter import executor

PROMPT = '>>> '
def output(output_string):
    print(output_string)
def print_welcome():
    version = 'List v1.0.0 (Python 3.8)'
    welcome = 'Welcome to Lisp REPL , Ctrl-C to Exit'
    output(version)
    output(welcome)
def print_prompt():
    token_input = input(PROMPT)
    return token_input
    
def get_tokens(token_input):
    tokenizer = token.Tokenizer(token_input)
    tokens = list()
    while not tokenizer.EOF:
        tokens.append(tokenizer.next_token())
    return tokens
        
def start():
    print_welcome()
    while True:
        token_input = print_prompt()
        tokens = get_tokens(token_input)[:-1]
        token_str = list(map(str,get_tokens(token_input)))
        # output(token_str)
        parser_instance = parser.Parser(tokens)
        remaining ,  parsed_representation = parser_instance.parse()
        # print(repr(parsed_representation))
        executor_instance = executor.Executor()
        print(executor_instance.exec(parsed_representation))


    

