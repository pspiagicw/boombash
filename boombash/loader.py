from boombash import executor, parser, token, tokenizer


def load(filename):
    """Load the given file into current session

    Arguments:
    filename: The filename to load , will only search in the current directory

    Returns:
    None

    It reads the file and does the standard procedure(Tokenize , Parse and Execute).
    Only used when executing a file , is not designed for importing stuff
    """
    data = None
    with open(filename) as inputfile:
        data = inputfile.read()
    tokenizer_instance = tokenizer.Tokenizer(data)
    tokens = list()
    while not tokenizer_instance.EOF:
        tokens.append(tokenizer_instance.next_token())
    parser_instance = parser.Parser(tokens)
    executor_instance = executor.Executor()
    remaining, parsed_representation = parser_instance.parse()
    while remaining:
        executor_instance.exec(parsed_representation)
        remaining, parsed_representation = parser_instance.parse(remaining)
