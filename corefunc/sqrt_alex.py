import sys


def sqrt(x):        # avoid catching type error
    """Compute squre roots using the method of Heron of Alexandria
        Args:
            x: the number of which the square root is to be computed
        Returns:
            the square root of x
        Raises:
            ValueError: If x is negative
    """

    guess = x
    i = 0
    try:
        if x < 0:
            raise ValueError('Cannot compute square root of ' f'negative number {x}')
        while guess * guess != 0 and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
        return guess
    except (ZeroDivisionError, ValueError) as e:
        print(f'calculation error: {e}', file=sys.stderr)
        # raise


def main():
    print(sqrt(9))
    print(sqrt(2))
    print(sqrt(-1))


if __name__ == '__main__':
    main()
