from rant_exceptions import RantParserException
from rant_token import *
from rant_object import RantBlockObject
import rant_parser as Parser


def build(tokens: list[RantToken]) -> RantBlockObject:
    choices = list()
    this_choice = list()
    if tokens[0].type is not RantTokenType.LEFT_CURLY_BRACKET:
        raise RantParserException(
            "[RantBlockFactory.build] block factory called without '{', this shouldn't happen!")
    tokens.pop(0)

    while len(tokens) > 0:
        token = tokens[0]
        tokens.pop(0)
        match token.type:
            case RantTokenType.PIPE:
                choices.append(Parser.parse(this_choice))
                continue
            case RantTokenType.RIGHT_CURLY_BRACKET:
                choices.append(Parser.parse(this_choice))
                return RantBlockObject(choices)
            case _:
                this_choice.append(token)
                continue
    # something went wrong, fall over
    raise RantParserException(
        "[RantBlockFactory.build] something went wrong, probably a missing '}'")