"""
    Author: Arpit Shah
    Date:   02/19/2017
"""

import sys

def convert(text, shift=0):
    """
        Takes plaintext as string and provides the corresponding
        numbers to each alphabetic character.
    """
    text = text.lower().replace(" ", "")
    print "Converting: " + text
    for char in text:
        print char + " = " + str(ord(char)-97 + shift)

if __name__ == "__main__":
    ARGS = sys.argv
    convert(ARGS[1])
