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

    if len(sentence) == 0:
        return (0, None)
    else:
        return len(sentence), sentence[0]
