import sys
from math import sqrt
from typing import List


def is_prime(x):
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def find_factors(x):
    factors: list[int] = []  # 'list[int]' is a type hint
    for i in range(2, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors


def input_checker(x):
    try:
        if x < 2:
            raise ValueError(f'number must be more than 2, invalid input {x}')
        return True
    except (TypeError, ValueError) as e:
        print(f'input error: {e}', file=sys.stderr)


def main(x: int):
    if input_checker(x):
        print(f'number {x} is {is_prime(x)}')
        print(f'factors of {x} are {find_factors(x)}')


if __name__ == '__main__':
    main(sys.argv[1])
