from lexer.lexer_tokens import RantToken, RantTokenType
import lexer.lexer as lexer


def test_angle_brackets():
    test_string = '<>'
    result = lexer.lex(test_string)

    expected_result = [RantToken(RantTokenType.LEFT_ANGLE_BRACKET), RantToken(RantTokenType.RIGHT_ANGLE_BRACKET)]

    assert len(result) == len(expected_result)
    for actual, expected in zip(result, expected_result):
        assert actual == expected


def test_square_brackets():
    test_string = '[]'
    result = lexer.lex(test_string)

    expected_result = [RantToken(RantTokenType.LEFT_SQUARE_BRACKET), RantToken(RantTokenType.RIGHT_SQUARE_BRACKET)]

    assert len(result) == len(expected_result)
    for actual, expected in zip(result, expected_result):
        assert actual == expected


def test_curly_brackets():
    test_string = '{}'
    result = lexer.lex(test_string)

    expected_result = [RantToken(RantTokenType.LEFT_CURLY_BRACKET), RantToken(RantTokenType.RIGHT_CURLY_BRACKET)]

    assert len(result) == len(expected_result)
    for actual, expected in zip(result, expected_result):
        assert actual == expected


def test_pipe():
    test_string = '|'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.PIPE)

    assert len(result) == 1
    assert result[0] == expected_result


def test_hyphen():
    test_string = '-'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.HYPHEN)

    assert len(result) == 1
    assert result[0] == expected_result


def test_semicolon():
    test_string = ';'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.SEMICOLON)

    assert len(result) == 1
    assert result[0] == expected_result


def test_colon():
    test_string = ':'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.COLON)

    assert len(result) == 1
    assert result[0] == expected_result


def test_double_colon():
    test_string = '::'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.DOUBLE_COLON)

    assert len(result) == 1
    assert result[0] == expected_result


def test_quote():
    test_string = '"'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.QUOTE)

    assert len(result) == 1
    assert result[0] == expected_result


def test_new_line():
    test_string = r'\n'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.NEW_LINE)

    assert len(result) == 1
    assert result[0] == expected_result


def test_indefinite_article():
    test_string = r'\a'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.LOWER_INDEFINITE_ARTICLE)

    assert len(result) == 1
    assert result[0] == expected_result


def test_slash():
    test_string = r'\\'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.BACKSLASH)

    assert len(result) == 1
    assert result[0] == expected_result


def test_digit():
    test_string = r'\d'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.DIGIT)

    assert len(result) == 1
    assert result[0] == expected_result


def test_plaintext():
    test_string = 'hello'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.PLAIN_TEXT, 'hello')

    assert len(result) == 1
    assert result[0] == expected_result


def test_exclamation_mark():
    test_string = '!'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.EXCLAMATION_MARK)

    assert len(result) == 1
    assert result[0] == expected_result


def test_equals():
    test_string = '='
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.EQUALS)

    assert len(result) == 1
    assert result[0] == expected_result


def test_dot():
    test_string = '.'
    result = lexer.lex(test_string)

    expected_result = RantToken(RantTokenType.DOT)

    assert len(result) == 1
    assert result[0] == expected_result


def test_long_string():
    test_string = 'angle brackets <:> curly brackets{ ::  } square brackets []plaintext-hello|'
    result = lexer.lex(test_string)

    expected_result = [RantToken(RantTokenType.PLAIN_TEXT, 'angle brackets '),
                       RantToken(RantTokenType.LEFT_ANGLE_BRACKET), RantToken(RantTokenType.COLON),
                       RantToken(RantTokenType.RIGHT_ANGLE_BRACKET),
                       RantToken(RantTokenType.PLAIN_TEXT, ' curly brackets'),
                       RantToken(RantTokenType.LEFT_CURLY_BRACKET), RantToken(RantTokenType.PLAIN_TEXT, ' '),
                       RantToken(RantTokenType.DOUBLE_COLON), RantToken(RantTokenType.PLAIN_TEXT, '  '),
                       RantToken(RantTokenType.RIGHT_CURLY_BRACKET),
                       RantToken(RantTokenType.PLAIN_TEXT, ' square brackets '),
                       RantToken(RantTokenType.LEFT_SQUARE_BRACKET), RantToken(RantTokenType.RIGHT_SQUARE_BRACKET),
                       RantToken(RantTokenType.PLAIN_TEXT, 'plaintext'), RantToken(RantTokenType.HYPHEN),
                       RantToken(RantTokenType.PLAIN_TEXT, 'hello'), RantToken(RantTokenType.PIPE)]

    assert len(result) == len(expected_result)
    for actual, expected in zip(result, expected_result):
        assert actual == expected


def test_realistic_sentence():
    test_string = r'I work as \a <noun-job>'
    result = lexer.lex(test_string)

    expected_result = [RantToken(RantTokenType.PLAIN_TEXT, "I work as "),
                       RantToken(RantTokenType.LOWER_INDEFINITE_ARTICLE), RantToken(RantTokenType.PLAIN_TEXT, " "),
                       RantToken(RantTokenType.LEFT_ANGLE_BRACKET), RantToken(RantTokenType.PLAIN_TEXT, "noun"),
                       RantToken(RantTokenType.HYPHEN), RantToken(RantTokenType.PLAIN_TEXT, "job"),
                       RantToken(RantTokenType.RIGHT_ANGLE_BRACKET)]

    assert len(result) == len(expected_result)
    for actual, expected in zip(result, expected_result):
        assert actual == expected
