#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string
    ...

    Parameters
    ----------
    my_string : str
        The string to remove 'Cc' from

    Return:
        The new string
    """

    return ("".join([c for c in my_string if c not in ['c', 'C']]))
