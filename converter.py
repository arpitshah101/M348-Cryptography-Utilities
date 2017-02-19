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

def affine(text, alpha, beta):
    """
        Takes plaintext, alpha and beta, and converts each letter
        to cipertext.
    """
    text = text.lower().replace(" ", "")
    print "Converting:         " + text
    print "Encryption formula: " + str(alpha) + "x" + " + " + str(beta)
    for char in text:
        print char + " = " + str(((ord(char)-97)*alpha + beta) % 26)

if __name__ == "__main__":
    ARGS = sys.argv
    if ARGS[1] == "affine":
        affine(ARGS[2], int(ARGS[3]), int(ARGS[4]))
    else:
        convert(ARGS[1])
