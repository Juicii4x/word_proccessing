"""
Beginning of psychological trauma
"""


def get_words(file):
    """
    function returns a list of all words from the read txt file
    args:: file - file directo
    returns:: a list of words...
    """
    f = open("words.txt", "r")
    words = f.read()
    f.close()
    return words


def cleaning_words(words):
    """
    function lowers all words
    args:: words list
    returns:: lowers words ready from processing
    """
