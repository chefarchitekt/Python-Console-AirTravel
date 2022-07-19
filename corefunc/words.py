"""Retrieve and print words from a URL

Usage:

    python3 words.py <URL>

"""

import sys
from urllib.request import urlopen


def fetch_words(url: str):
    """Fetch a list of words from a URL, str object

        Args:
            url: The URL of a UTF-8 text document.

        Returns:
            A list of strings containing the words from the document.

    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    """Print items one per line.

        Args:
            An iterable series of printable items

    """
    for item in items:
        print(item)


# print(__name__)
# if when importing, the function emit '__main__' means this function is imported to another module

# if __name__ == '__main__':
#    fetch_words()

def main(url: str):
    """Print each word from a text document from a URL.
        Args:
            url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)    # sys expects the 0th arg is the module filename
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])

# we could use shebang for auto executing this module
# this means program loaders will use shebang to determine the correct compiler or interpreter
# this is only applicable for mac, unix, and linux systems
# as for windows, there is a workaround using PyLauncher library

# first mark the at the top of the file with #! use/bin/env python3
    # the mac or linux os will choose the compiler stated in shebang to execute the script
# second, use chmod to transform the file as executable
    # chmod +x words.py
# at terminal prompt we could directly execute the file as follow:
    # ./words.py http://sixty-north.com/c/t.txt
