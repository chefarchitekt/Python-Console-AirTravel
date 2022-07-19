import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def convert(s):
    # x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        return x
        # print(f'conversion succeeded! x = {x}')
    except (KeyError, TypeError) as e:
        # print('conversion failed')  # if we remove this statement, it will produce error
        # empty block is not permitted
        # empty block is not permitted, use 'pass' a no-op syntactically permissible blocks
        # that are semantically empty

        print(f'Conversion Error: {e!r}', file=sys.stderr)  # f'{exp!r} repr will be outputted
        # return -1
        raise


def string_log(s):
    v = convert(s)
    return log(v)  # compute natural log
