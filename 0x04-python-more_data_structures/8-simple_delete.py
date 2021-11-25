#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary
    key : string
        argument will be always a string

    Return:
        the new dictionary
    """

    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
