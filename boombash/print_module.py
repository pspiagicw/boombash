
from boombash import token
def stdout(input_object):
    if isinstance(input_object , token.Token):
        print(input_object.Literal)
    else:
        print(input_object)
