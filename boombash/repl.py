import pprint
from boombash import token
from boombash import parser
from boombash import executor
from boombash import tokenizer

PROMPT = ">>> "


def output(output_string):
    print(output_string)


def print_welcome():
    version = "BoomBash v1.0.0 (Python 3.8)"
    welcome = "Welcome to Lisp REPL , Ctrl-C to Exit"
    output(version)
    output(welcome)


def print_prompt():
    token_input = input(PROMPT)
    return token_input


def get_tokens(token_input):
    tokenizer_instance = tokenizer.Tokenizer(token_input)
    tokens = list()
    while not tokenizer_instance.EOF:
        tokens.append(tokenizer_instance.next_token())
    return tokens


def start():
    print_welcome()
    variables = dict()
    functions = dict()
    while True:
        token_input = print_prompt()
        tokens = get_tokens(token_input)[:-1]
        token_str = list(map(str, get_tokens(token_input)))
        parser_instance = parser.Parser(tokens)
        remaining, parsed_representation = parser_instance.parse()
        executor_instance = executor.Executor(variables, functions)
        output = executor_instance.exec(parsed_representation)
        variables, functions = executor_instance.variables, executor_instance.functions
        if output:
            print(output)
