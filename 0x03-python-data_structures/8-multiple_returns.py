#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character
    ...

    Parameters
    ----------
    sentence : str
        The string to treat

    Return:
        A tuple
    """

    return (0, None) if len(sentence) == 0 else len(sentence), sentence[0]
